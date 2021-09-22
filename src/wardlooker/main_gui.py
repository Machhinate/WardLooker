import sys

from WardLooker import WardLooker
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, \
    QGridLayout
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore

widgets = {"logo": [],
           "Button": [],
           "score": [],
           "question": []}


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("Ward Looker")

    label = QtWidgets.QLabel(win)
    label.setText("labman")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())


app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("Ward Looker")
win.setFixedWidth(1000)
win.move(2700, 200)
win.setStyleSheet("background: #161219;")

grid = QGridLayout()

def frame1():
    #logo
    image = QPixmap("C:/Users/micah/OneDrive/Desktop/WardLooker/src/Icon.png")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    #button widget
    button = QPushButton("play")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 45px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 0;" +
        "margin: 100px 200px;}" +
        "*:hover{background: '#BC006C';}"
    )
    widgets["Button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 0)
    grid. addWidget(widgets["button"][-1], 1, 0)

def frame2():
    score = QLabel("80")
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(f"""
        font-size: 35px;
        color: 'white';
        padding: 25px 20px 0px 20px;
        margin: 20px 200px;
        background: '#64A314';
        border: 1px solid '#64A314';
        border-radius: 40px;""")

    widgets["score"].append(score)

    question = QLabel("placeholder text")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: Shanti;" +
        "font-size: 25px;" +
        "color: 'white';" +
        "padding: 75px;"
    )
    widgets["question"].append(question)

    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)


frame2()

win.setLayout(grid)

win.show()
sys.exit(app.exec_())


