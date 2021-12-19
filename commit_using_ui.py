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
        

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.days = 8
        self.weeks = 53

        self.selected_days = []
        
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.layout = QGridLayout(centralWidget)

        for row in range(1, self.days): 
           for column in range(0, self.weeks):
                buttonname = row + column * 7
                button = PushButton(f'{buttonname}', self)
                button.clicked.connect(partial(self.onClicked, buttonname, button))
                button.setStyleSheet(f"""background-color: lightgrey""")
                self.layout.addWidget(button, row, column)
        
        buttonname = 'push'
        button = PushButton(f'{buttonname}', self)
        button.clicked.connect(partial(self.onClickedSend))
        button.setStyleSheet(f"""background-color: lightgrey""")
        self.layout.addWidget(button, 8, 0, 1, 2)

    def checkForDateInList(self, date):
        if str(date) in self.selected_days:
            self.selected_days.remove(str(date))
            colorReturn = 'lightgrey'
        else:
            self.selected_days.append(str(date))
            colorReturn = 'green'

        return colorReturn

    def onClicked(self, name, button):
        my_date = datetime.strptime(str.rstrip("2020-12-20"), '%Y-%m-%d')
        selected_date = my_date + timedelta(days=name-1)
        print(selected_date)
        color = self.checkForDateInList(selected_date)
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