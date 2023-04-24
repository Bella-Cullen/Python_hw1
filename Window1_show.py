from PyQt5.QtGui import QPalette, QPixmap, QBrush
from PyQt5.QtWidgets import *

# 待做:搞个下拉框显示历史搜索记录
class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home of Football Lover")
        self.resize(1200, 800)
        self.move(300,100)

        palette=QPalette()
        pix=QPixmap("C:/Users/ASUS/Desktop/background.jpg")
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background,QBrush(pix))
        self.setPalette(palette)

        self.txt=self.input()
        self.btn=self.search()

    def input(self):
        text=QLineEdit(self)
        text.move(400,200)
        text.resize(400,50)
        text.setPlaceholderText("请输入你喜爱的球员:")
        text.setClearButtonEnabled(True)
        return text

    def search(self):
        butn=QPushButton(self)
        butn.setText("搜索")
        butn.move(800,200)
        butn.resize(100,50)
        return butn
