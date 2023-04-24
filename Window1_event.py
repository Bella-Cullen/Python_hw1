import re
import requests
from bs4 import BeautifulSoup

from Window1_show import Window1


class Page1(Window1):
    def __init__(self):
        super().__init__()
        self.btn.clicked.connect(lambda: self.obtain_input())

    def obtain_input(self):
        webpage1 = Webpage1(self.txt.text())  # self.txt.text() is the input of the searching
        self.player_lst = webpage1.player_list


# get players` name list
class Webpage1:
    def __init__(self, str):
        self.player_name = str
        self.url = "https://www.whoscored.com/Search/?t=" + str
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
        self.html_ = requests.get(url=self.url, headers=self.headers)
        self.html = self.html_.text
        self.soup = BeautifulSoup(self.html, 'lxml')
        self.player_list = self.soup.find_all('a', href=re.compile("Player"))
