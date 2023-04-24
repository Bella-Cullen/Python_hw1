from PyQt5.QtGui import QPalette, QPixmap, QBrush
from PyQt5.QtWidgets import *


# to do:display searching history
class Window1(QWidget):
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
        self.txt = self.input()
        self.btn = self.search()

    # searching box
    def input(self):
        text = QLineEdit(self)
        text.move(400, 200)
        text.resize(400, 50)
        text.setPlaceholderText("请输入你喜爱的球员:")
        text.setClearButtonEnabled(True)
        return text

    # searching button
    def search(self):
        butn = QPushButton(self)
        butn.setText("搜索")
        butn.move(800, 200)
        butn.resize(100, 50)
        return butn
