from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette, QPixmap, QBrush

class Window3(QWidget):
    def __init__(self):
        #basic settings
        super().__init__()
        self.setWindowTitle("Simple Player Dictionary")
        self.resize(1200, 800)
        self.move(300, 100)

        #background setting
        palette = QPalette()
        pix = QPixmap("C:/Users/ASUS/Desktop/python_hw1/Python_hw1/background.jpg")
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

        #elements settings
        self.btn_return = self.return_()
        self.name=self.attribute_show(0)
        self.player_picture=self.attribute_show(1)
        self.team=self.attribute_show(2)
        self.team_picture=self.attribute_show(3)
        self.full_name=self.attribute_show(4)
        self.age=self.attribute_show(5)
        self.birthday=self.attribute_show(6)
        self.height=self.attribute_show(7)
        self.nation=self.attribute_show(8)
        self.position_lst=self.attribute_show(9)

    #button returning to page2
    def return_(self):
        butn=QPushButton(self)
        butn.setText("返回")
        butn.move(100,100)
        butn.resize(100,50)
        return butn

    def attribute_show(self,num):
        content=QLabel(self)
        content.setText("")
        content.setAlignment(QtCore.Qt.AlignLeft)
        if num==0:
            content.setGeometry(400,100,400,100)
            content.setFont(QFont('Times', 20, QFont.Black))
            content.setAlignment(QtCore.Qt.AlignCenter)
            content.setAlignment(QtCore.Qt.AlignTop)
        elif num==1:
            content.setGeometry(850,100,200,300)
        elif num==3:
            content.setGeometry(250,100,100,100)
        elif num==2:
            content.setGeometry(100,250,550,50)
            content.setFont(QFont('Times', 10, QFont.Black))
        elif num==9:
            content.setGeometry(100, 100 + 50 * num, 550, 200)
            content.setFont(QFont('Times', 10, QFont.Black))
            content.setWordWrap(True)
        else:
            content.setGeometry(100,100+50*num,550,50)
            content.setFont(QFont('Times', 10, QFont.Black))
        return content