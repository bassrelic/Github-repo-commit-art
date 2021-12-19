import sys
from functools import partial
from PyQt5.Qt import QApplication, QMainWindow, QPushButton, QWidget, QLabel, Qt, QFont, QGridLayout, QSize
from datetime import datetime, timedelta
import os


class PushButton(QPushButton):
    def __init__(self, text, parent=None):
        super(PushButton, self).__init__(text, parent)

        self.text = text

        self.setText(text)
        self.setMaximumSize(QSize(20, 20))
        self.setContentsMargins(10,10,10,10)

class Label(QLabel):
    def __init__(self, text, parent=None):
        super(Label, self).__init__(text, parent)

        self.text = text

        self.setText(text)
        self.setMaximumSize(QSize(20, 20))
        self.setContentsMargins(10,10,10,10)


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.rows = 9
        self.cols = 53

        self.selected_days = []

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.setStyleSheet(f"""background-color: lightgrey""")

        self.layout = QGridLayout(centralWidget)

        today = datetime.today()
        my_date = datetime.strptime(str.rstrip("2020-12-20"), '%Y-%m-%d')
        month = my_date.strftime('%b')
        label = Label(f'{month}')
        self.layout.addWidget(label, 0, 0)

        for row in range(2, self.days): 
           for column in range(0, self.weeks):
                button_date = my_date + timedelta(row - 1 + column * 7 - 1)

                if button_date <= today:
                    button = PushButton(f'{button_date}', self)
                    button.clicked.connect(partial(self.onClicked, button_date, button))
                    button.setStyleSheet(f"""background-color: #ebedf0""")
                    self.layout.addWidget(button, row, column)

                    if button_date.strftime('%b') != month and row == 2:
                        month = button_date.strftime('%b')
                        label = Label(f'{month}')
                        self.layout.addWidget(label, 0, column)

        buttonname = 'push'
        button = PushButton(f'{buttonname}', self)
        button.clicked.connect(partial(self.onClickedSend))
        button.setStyleSheet(f"""background-color: #ebedf0""")
        self.layout.addWidget(button, 8, 0, 1, 2)

    def checkForDateInList(self, date):
        if str(date) in self.selected_days:
            self.selected_days.remove(str(date))
            colorReturn = '#ebedf0'
        else:
            self.selected_days.append(str(date))
            colorReturn = '#40c463'

        return colorReturn

    def onClicked(self, name, button):
        print(name)
        color = self.checkForDateInList(name)
        button.setStyleSheet(f"""background-color: {color}""")

    def onClickedSend(self):
        self.selected_days.sort()
        print(self.selected_days)

        for day in self.selected_days:
            readmeFile = open('README.md', 'a')
            readmeFile.write(str(day) + '\n')
            readmeFile.close()
            os.system("git add README.md")
            commitMessage = f"""git commit -m "Add date {day} to README" --date="{day}" """
            os.system(commitMessage)
        os.system("git push")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle('GitHub Art by Pixel')
    w.show()
    sys.exit(app.exec_())