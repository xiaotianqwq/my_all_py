# -*- coding = utf-8 -*-
# @Time:2022/6/25 20:06
# @Author:宇
# @File:QQ机器人.py
# @Software:PyCharm
import requests

url = 'https://qmsg.zendee.cn:443/group/9a753457490a93cfa9d17d4b5a1656a1'

data = {
    'msg': '1111',
    'qq': '920039461'
}
res = requests.post(url=url,data=data).json()
print(res)