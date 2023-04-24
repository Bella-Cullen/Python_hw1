import re
import requests
from PyQt5.QtGui import QPixmap

from Window3_show import Window3


class Page3(Window3):
    def __init__(self):
        super().__init__()
        self.attribute_lst = []
        self.player_picture_lst = []
        self.team_picture_lst = []

    def initial(self):
        i = 0  # current index of the attributes` list

        x_player_picture = re.search('src="(.*)" style', str(self.player_picture_lst[0]))
        player_picture_url = x_player_picture.group(1)
        x_team_picture = re.search('src="(.*)" width', str(self.team_picture_lst[0]))
        team_picture_url = x_team_picture.group(1)

        x_name = re.search('</span>(.*)\n.*</div>', str(self.attribute_lst[i]))
        name = x_name.group(1)
        i += 1

        x_full_name = re.search('</span>(.*)\n.*</div>', str(self.attribute_lst[i]))
        if x_full_name != None:
            full_name = x_full_name.group(1)
            i += 1
        else:
            full_name = name

        x_team = re.search('>(.*)</a>', str(self.attribute_lst[i]))
        if x_team != None:
            team = x_team.group(1)
            i += 1
        else:
            team = "Unknown"

        x_shirt = re.search('Shirt', str(self.attribute_lst[i]))
        if x_shirt != None:
            i += 1

        x_age = re.search('</span>(.*) years.*<i>(.*)-(.*)-(.*)</i>', str(self.attribute_lst[i]))
        if x_age != None:
            age = x_age.group(1)
            birthday = (x_age.group(4), x_age.group(3), x_age.group(2))
            i += 1
        else:
            age = "Unknown"
            birthday = ("Unknown", "Unknown", "Unknown")

        x_height = re.search('</span>(.*)</div>', str(self.attribute_lst[i]))
        if x_height != None:
            height = x_height.group(1)
            i += 1
        else:
            height = "Unknown"

        x_nation = re.search('left">(.*)<span', str(self.attribute_lst[i]))
        if x_nation != None:
            nation = x_nation.group(1)
            i += 1
        else:
            nation = "Unknown"

        positions_lst = re.findall('inline-block;">(.*)?</span>', str(self.attribute_lst[i]))

        self.name.setText(name)
        self.full_name.setText("全名:    " + full_name)
        self.team.setText("俱乐部:  " + team)
        self.age.setText("年龄:    " + age)
        self.birthday.setText("出生年月:" + birthday[0] + "-" + birthday[1] + "-" + birthday[2])
        self.height.setText("身高:    " + height)
        self.nation.setText("国籍:    " + nation)
        str1 = ''.join(positions_lst)
        self.position_lst.setText("场上位置:" + str1)

        # get the player`s picture and team`s picture to files and display them
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
        img = requests.get(url=player_picture_url, headers=headers)
        with open("C:/Users/ASUS/Desktop/python_hw1/Python_hw1/player_pic.jpg", "wb") as f:
            f.write(img.content)
        self.player_picture.setPixmap(QPixmap("C:/Users/ASUS/Desktop/python_hw1/Python_hw1/player_pic.jpg"))
        img2 = requests.get(url=team_picture_url, headers=headers)
        with open("C:/Users/ASUS/Desktop/python_hw1/Python_hw1/team_pic.jpg", "wb") as f2:
            f2.write(img2.content)
        self.team_picture.setPixmap(QPixmap("C:/Users/ASUS/Desktop/python_hw1/Python_hw1/team_pic.jpg"))
