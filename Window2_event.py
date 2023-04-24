import re
import requests
from bs4 import BeautifulSoup

from Window2_show import Window2


class Page2(Window2):
    def __init__(self):
        super().__init__()
        self.player_lst = []
        for i in range(20):
            self.show_player_lst[i].setOpenExternalLinks(False)  # hyperlinks jumping disabled

        # 20 players displayed at the same time at most
        self.show_player_lst[0].linkActivated.connect(self.link_clicked_0)
        self.show_player_lst[1].linkActivated.connect(self.link_clicked_1)
        self.show_player_lst[2].linkActivated.connect(self.link_clicked_2)
        self.show_player_lst[3].linkActivated.connect(self.link_clicked_3)
        self.show_player_lst[4].linkActivated.connect(self.link_clicked_4)
        self.show_player_lst[5].linkActivated.connect(self.link_clicked_5)
        self.show_player_lst[6].linkActivated.connect(self.link_clicked_6)
        self.show_player_lst[7].linkActivated.connect(self.link_clicked_7)
        self.show_player_lst[8].linkActivated.connect(self.link_clicked_8)
        self.show_player_lst[9].linkActivated.connect(self.link_clicked_9)
        self.show_player_lst[10].linkActivated.connect(self.link_clicked_10)
        self.show_player_lst[11].linkActivated.connect(self.link_clicked_11)
        self.show_player_lst[12].linkActivated.connect(self.link_clicked_12)
        self.show_player_lst[13].linkActivated.connect(self.link_clicked_13)
        self.show_player_lst[14].linkActivated.connect(self.link_clicked_14)
        self.show_player_lst[15].linkActivated.connect(self.link_clicked_15)
        self.show_player_lst[16].linkActivated.connect(self.link_clicked_16)
        self.show_player_lst[17].linkActivated.connect(self.link_clicked_17)
        self.show_player_lst[18].linkActivated.connect(self.link_clicked_18)
        self.show_player_lst[19].linkActivated.connect(self.link_clicked_19)

    def initial(self):
        if self.player_lst == []:  # no player meet searching requirement
            self.empty()
        else:
            self.not_empty()

    def empty(self):
        self.prompt.setText("未找到符合条件的球员")
        for i in range(20):
            self.show_player_lst[i].setVisible(False)

    def not_empty(self):
        self.prompt.setText("找到以下球员")
        length = len(self.player_lst)
        if length > 20:
            length = 20
        for i in range(length):  # show all players` names
            x = re.search('href="(.*/Show/(.*))"><span', str(self.player_lst[i]))
            url2 = x.group(1)
            player_name = x.group(2)
            url = "https://www.whoscored.com" + url2
            text = "<A href='" + url + "'>" + str(i + 1) + ". " + player_name + "</A>"
            self.show_player_lst[i].setText(text)
            self.show_player_lst[i].setVisible(True)

        for i in range(length, 20):
            self.show_player_lst[i].setVisible(False)

    def link_clicked_0(self):
        webpage2 = Webpage2(self.show_player_lst[0].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_1(self):
        webpage2 = Webpage2(self.show_player_lst[1].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_2(self):
        webpage2 = Webpage2(self.show_player_lst[2].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_3(self):
        webpage2 = Webpage2(self.show_player_lst[3].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_4(self):
        webpage2 = Webpage2(self.show_player_lst[4].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_5(self):
        webpage2 = Webpage2(self.show_player_lst[5].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_6(self):
        webpage2 = Webpage2(self.show_player_lst[6].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_7(self):
        webpage2 = Webpage2(self.show_player_lst[7].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_8(self):
        webpage2 = Webpage2(self.show_player_lst[8].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_9(self):
        webpage2 = Webpage2(self.show_player_lst[9].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_10(self):
        webpage2 = Webpage2(self.show_player_lst[10].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_11(self):
        webpage2 = Webpage2(self.show_player_lst[11].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_12(self):
        webpage2 = Webpage2(self.show_player_lst[12].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_13(self):
        webpage2 = Webpage2(self.show_player_lst[13].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_14(self):
        webpage2 = Webpage2(self.show_player_lst[14].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_15(self):
        webpage2 = Webpage2(self.show_player_lst[15].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_16(self):
        webpage2 = Webpage2(self.show_player_lst[16].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_17(self):
        webpage2 = Webpage2(self.show_player_lst[17].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_18(self):
        webpage2 = Webpage2(self.show_player_lst[18].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst

    def link_clicked_19(self):
        webpage2 = Webpage2(self.show_player_lst[19].text())
        self.attribute_lst = webpage2.attribute_lst
        self.player_picture_lst = webpage2.player_picture_lst
        self.team_picture_lst = webpage2.team_picture_lst


# get player`s attributes(name,full name,age,etc.)
class Webpage2:
    def __init__(self, str):
        x = re.search("'(.*)'", str)
        self.url = x.group(1)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
        self.html_ = requests.get(url=self.url, headers=self.headers)
        self.html = self.html_.text
        self.soup = BeautifulSoup(self.html, 'lxml')
        self.player_picture_lst = self.soup.find_all('img', {'class': 'player-picture'})
        self.team_picture_lst = self.soup.find_all('img', {'class': 'team-emblem'})
        self.attribute_lst = self.soup.find_all('div', {'class': 'col12-lg-6 col12-m-6 col12-s-6 col12-xs-12'})
