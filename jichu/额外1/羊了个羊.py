# -*- coding = utf-8 -*-
# @Time:2022/9/16 16:36
# @Author:宇
# @File:羊了个羊.py
# @Software:PyCharm
import time

import requests

headers = {
    "Accept-Encoding": "gzip,compress,br,deflate",
    "Accept": "*/*",
    "Connection": "keep-alive",
    "t": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ0MjA2OTAsIm5iZiI6MTY2MzMxODQ5MCwiaWF0IjoxNjYzMzE2NjkwLCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjoyOTY3MDI5MCwiZGVidWciOiIiLCJsYW5nIjoiIn0.jqdN5wBHoOkYcrZ-77vThlpgMc3glvzGmVQKTlPJdvo",
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.26(0x18001a34) NetType/WIFI Language/zh_CN"
}
cookies = {}


def testRequest():
    url = 'http://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time=0&rank_role=1&skin=1'
    wb_data = requests.get(url, headers=headers)
    print("code:", wb_data.status_code)


if __name__ == '__main__':
    # 循环次数想刷多少次
    for lp in range(1):
        testRequest()
        # time.sleep(1)