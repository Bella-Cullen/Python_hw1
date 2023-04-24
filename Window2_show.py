from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QBrush


class Window2(QWidget):
    def __init__(self):
        # basic settings
        super().__init__()
        self.setWindowTitle("Simple Player Dictionary")
        self.resize(1200, 800)
        self.move(300, 100)

        # background setting
        palette = QPalette()
        pix = QPixmap("C:/Users/ASUS/Desktop/python_hw1/Python_hw1/background.jpg")
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

        # elements settings
        self.prompt = self.prompt_()
        self.btn_return = self.return_()
        self.player1 = self.player_show(1)
        self.player2 = self.player_show(2)
        self.player3 = self.player_show(3)
        self.player4 = self.player_show(4)
        self.player5 = self.player_show(5)
        self.player6 = self.player_show(6)
        self.player7 = self.player_show(7)
        self.player8 = self.player_show(8)
        self.player9 = self.player_show(9)
        self.player10 = self.player_show(10)
        self.player11 = self.player_show(11)
        self.player12 = self.player_show(12)
        self.player13 = self.player_show(13)
        self.player14 = self.player_show(14)
        self.player15 = self.player_show(15)
        self.player16 = self.player_show(16)
        self.player17 = self.player_show(17)
        self.player18 = self.player_show(18)
        self.player19 = self.player_show(19)
        self.player20 = self.player_show(20)
        self.show_player_lst = [self.player1, self.player2, self.player3, self.player4,
                                self.player5, self.player6, self.player7, self.player8,
                                self.player9, self.player10, self.player11, self.player12,
                                self.player13, self.player14, self.player15, self.player16,
                                self.player17, self.player18, self.player19, self.player20, ]

    # prompt displaying whether there are players meeting searching requirement
    def prompt_(self):
        text = QLabel(self)
        text.setText("")
        text.setGeometry(300, 100, 600, 50)
        text.setFont(QFont('Times', 14, QFont.Black))
        text.setAlignment(QtCore.Qt.AlignCenter)
        return text

    # button returning to page1
    def return_(self):
        butn = QPushButton(self)
        butn.setText("返回")
        butn.move(100, 100)
        butn.resize(100, 50)
        return butn

    # texts of player names
    # hyperlink,click them and jump to page3
    def player_show(self, num):
        text = QLabel(self)
        text.setText("")
        text.setGeometry(100 if num <= 10 else 600, 200 + 50 * ((num - 1) % 10), 500, 50)
        text.setFont(QFont('Times', 10, QFont.Black))
        text.setAlignment(QtCore.Qt.AlignLeft)
        return text
