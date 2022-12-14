# -*- coding = utf-8 -*-
# @Time:2022/4/30 13:55
# @Author:宇
# @File:钉钉机器人.py
# @Software:PyCharm
import requests
import json


headers = {
    'Content-Type': 'application/json'
}
text ={
    "text": {
        "content": "我就是我, @180xxxxxx 是不一样的烟火"
    },
    "msgtype": "text"
}

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=dc4220e7d5394b63f7015eb812ab9c03acf932ca4f195e69d52772a340fff7d5'
res = requests.post(url=webhook, data=json.dumps(text),headers=headers).text
print(res)