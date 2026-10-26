from datetime import datetime

import pytest

import commit_using_ui


@pytest.fixture(scope="session")
def application():
    return commit_using_ui.QApplication.instance() or commit_using_ui.QApplication([])


@pytest.fixture
def window(application):
    result = commit_using_ui.MyWindow("2024-01-01")
    yield result
    result.close()


def test_check_for_date_in_list_toggles_selection_and_color(window):
    date = datetime(2024, 1, 1)

    assert window.check_for_date_in_list(date) == "#40c463"
    assert window.selected_days == [str(date)]
    assert window.check_for_date_in_list(date) == "#ebedf0"
    assert window.selected_days == []


def test_clicking_date_button_toggles_selection_and_button_color(window, capsys):
    button = window.layout.itemAtPosition(1, 0).widget()

    button.click()

    assert window.selected_days == ["2024-01-01 00:00:00"]
    assert "background-color: #40c463" in button.styleSheet()
    assert capsys.readouterr().out.strip() == "2024-01-01 00:00:00"

    button.click()

    assert window.selected_days == []
    assert "background-color: #ebedf0" in button.styleSheet()


def test_window_only_displays_dates_through_today(application, monkeypatch):
    class FixedDateTime(datetime):
        @classmethod
        def today(cls):
            return cls(2024, 1, 10)

    monkeypatch.setattr(commit_using_ui, "datetime", FixedDateTime)
    window = commit_using_ui.MyWindow("2024-01-01")
    try:
        assert window.layout.itemAtPosition(1, 0).widget().text == "2024-01-01 00:00:00"
        assert window.layout.itemAtPosition(3, 1).widget().text == "2024-01-10 00:00:00"
        assert window.layout.itemAtPosition(4, 1) is None
    finally:
        window.close()


def test_send_appends_dates_and_runs_git_commands_in_sorted_order(
    window, monkeypatch, tmp_path
):
    monkeypatch.chdir(tmp_path)
    readme = tmp_path / "README.md"
    readme.write_text("existing\n", encoding="utf-8")
    commands = []
    monkeypatch.setattr(commit_using_ui.os, "system", commands.append)
    window.selected_days = [
        "2024-01-03 00:00:00",
        "2024-01-01 00:00:00",
    ]

    window.on_clicked_send()

    assert window.selected_days == [
        "2024-01-01 00:00:00",
        "2024-01-03 00:00:00",
    ]
    assert readme.read_text(encoding="utf-8") == (
        "existing\n2024-01-01 00:00:00\n2024-01-03 00:00:00\n"
    )
    assert commands == [
        "git add README.md",
        'git commit -m "Add date 2024-01-01 00:00:00 to README" '
        '--date="2024-01-01 00:00:00" ',
        "git add README.md",
        'git commit -m "Add date 2024-01-03 00:00:00 to README" '
        '--date="2024-01-03 00:00:00" ',
        "git push",
    ]


def test_send_with_no_selected_dates_only_pushes(window, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    commands = []
    monkeypatch.setattr(commit_using_ui.os, "system", commands.append)

    window.on_clicked_send()

    assert not (tmp_path / "README.md").exists()
    assert commands == ["git push"]
