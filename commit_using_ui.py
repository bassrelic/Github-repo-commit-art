"""This module creates a ui with buttons, clicking the buttons lets you select on which
 dates to commit. Pressing the push button (bottom left) will cause commits and a push."""
import sys
import re
import os
from datetime import datetime, timedelta
from functools import partial
import argparse
from PyQt5.Qt import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QGridLayout, QSize


# pylint: disable=too-few-public-methods
class PushButton(QPushButton):
    """This class is used to define the buttons of this application."""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.text = text

        self.setText(text)
        self.setMaximumSize(QSize(20, 20))
        self.setContentsMargins(10,10,10,10)

# pylint: disable=too-few-public-methods
class Label(QLabel):
    """This class is used to define the labels showing months above the buttons."""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.text = text

        self.setText(text)
        self.setMaximumSize(QSize(20, 20))
        self.setContentsMargins(10,10,10,10)


class MyWindow(QMainWindow):
    """This class is used to define the mian window of this application."""
    def __init__(self, date):
        super().__init__()

        self.rows = 9
        self.cols = 53

        self.selected_days = []

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("background-color: lightgrey")

        self.layout = QGridLayout(central_widget)

        today = datetime.today()
        my_date = datetime.strptime(str.rstrip(date), '%Y-%m-%d')
        month = my_date.strftime('%b')
        label = Label(f'{month}')
        self.layout.addWidget(label, 0, 0)

        for row in range(1, self.rows - 1):
            for column in range(0, self.cols):
                button_date = my_date + timedelta(row + column * 7 - 1)

                if button_date <= today:
                    button = PushButton(f'{button_date}', self)
                    button.clicked.connect(partial(self.on_clicked, button_date, button))
                    button.setStyleSheet("background-color: #ebedf0")
                    self.layout.addWidget(button, row, column)

                    if button_date.strftime('%b') != month and row == 2:
                        month = button_date.strftime('%b')
                        label = Label(f'{month}')
                        self.layout.addWidget(label, 0, column)

        buttonname = 'push'
        button = PushButton(f'{buttonname}', self)
        button.clicked.connect(partial(self.on_clicked_send))
        button.setStyleSheet("background-color: #ebedf0")
        self.layout.addWidget(button, 8, 0, 1, 2)

    def check_for_date_in_list(self, date):
        """This method checks if the given date is already present in the list of dates.
        If it is not, it is added and a green color is returned.
        If it is, it is removed and a white color is returned."""
        if str(date) in self.selected_days:
            self.selected_days.remove(str(date))
            color_return = '#ebedf0'
        else:
            self.selected_days.append(str(date))
            color_return = '#40c463'

        return color_return

    def on_clicked(self, name, button):
        """This method prints the selected date for reference and checks if the date is
        already choosen. Depending if it was choosen previously, the color of the button
        is adjusted."""
        print(name)
        color = self.check_for_date_in_list(name)
        button.setStyleSheet(f"""background-color: {color}""")

    def on_clicked_send(self):
        """This method sorts the selected days, adds them to the readme for later
        reference and causes commits for every date. When all dates have ben committed,
        the changes are pushed."""
        self.selected_days.sort()
        print(self.selected_days)

        for day in self.selected_days:
            with open('README.md', 'a', encoding="utf-8") as readme_file:
                readme_file.write(str(day) + '\n')

            os.system("git add README.md")
            commit_message = f"""git commit -m "Add date {day} to README" --date="{day}" """
            os.system(commit_message)

        os.system("git push")

if __name__ == '__main__':
    date=""
    parser = argparse.ArgumentParser("commit_using_ui.py")
    parser.add_argument("date",
        help="The first date shown on your contribution matrix using the form yyyy-mm-dd.",
        metavar=date)
    args = parser.parse_args()
    r = re.compile("\\d{4}-\\d{2}-\\d{2}")

    if r.match(args.date) is None:
        print("Supplied Starting Date does not match the form yyy-mm-dd. Aborting!")
        sys.exit()

    print("Startig Date: " + args.date)

    app = QApplication(sys.argv)
    w = MyWindow(args.date)
    w.setWindowTitle('GitHub Art by Pixel')
    w.show()
    sys.exit(app.exec_())
