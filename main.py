from PyQt5.QtWidgets import *
import sys
from Window1_event import Page1
from Window2_event import Page2
from Window3_event import Page3

def page1_to_2(page1,page2):
    page2.player_lst=page1.player_lst
    page2.initial()
    page1.close()
    page2.show()

def page2_to_1(page1,page2):
    page2.close()
    page1.show()

def page2_to_3(page2,page3):
    page3.attribute_lst=page2.attribute_lst
    page3.player_picture_lst=page2.player_picture_lst
    page3.team_picture_lst=page2.team_picture_lst
    page3.initial()
    page2.close()
    page3.show()

def page3_to_2(page2,page3):
    page3.close()
    page2.show()

app = QApplication(sys.argv)
page1=Page1()
page1.show()
page2=Page2()
page3=Page3()
page1.btn.clicked.connect(lambda:page1_to_2(page1,page2))
page2.btn_return.clicked.connect(lambda:page2_to_1(page1,page2))
for i in range(20):
    page2.show_player_lst[i].linkActivated.connect(lambda:page2_to_3(page2,page3))
page3.btn_return.clicked.connect(lambda:page3_to_2(page2,page3))
sys.exit(app.exec_())