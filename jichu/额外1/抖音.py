# -*- coding = utf-8 -*-
# @Time:2022/7/12 9:32
# @Author:宇
# @File:抖音.py
# @Software:PyCharm
import json
import requests
import jsonpath

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
}
# https://www.douyin.com/web/api/v2/aweme/iteminfo/?item_ids=6997710927701216550
url = "https://www.douyin.com/web/api/v2/aweme/iteminfo/?item_ids=7149110111447813413"  # 此处是短视频的分享链接
session = requests.Session()
req = session.get(url, timeout=5, headers=headers)
# print(req.text)
unicodestr = json.loads(req.text)
print(unicodestr)

name = jsonpath.jsonpath(unicodestr, "$.item_list..cha_list..cha_name")[0]
play_addr = jsonpath.jsonpath(unicodestr, "$.item_list..video.play_addr.url_list")[0][0]  # 播放地址
# print(name)
print(play_addr)
addr = play_addr.replace("/playwm/", "/play/")  # 改写地址，变为无水印地址
# print(addr)
videoBin = session.get(addr, timeout=5, headers=headers)
with open(name + '.mp4', 'wb') as fb:
    fb.write(videoBin.content)
    print('下载完成，名称为:%s.mp4' % name)