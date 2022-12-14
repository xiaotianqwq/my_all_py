# -*- conding = utf-8 -*-
# @Time:2022/3/29 21:02
# @Author:宇
# @Flie:彩虹屁文案.py
# @Software:PyCharm

import requests


def get_sen():
    url = 'https://api.iyk0.com/chp'
    res = requests.get(url=url).json()
    sen = res['txt']
    return sen


def send(sen):
    sendkey = 'SCT114686T3reNzoXK89QsVIYmz6Dx5MN2'
    url = f'https://sctapi.ftqq.com/{sendkey}.send'
    data = {
        'title': '每日笑话',
        'desp': sen
    }
    requests.post(url=url,data=data)


def main():
    sen = get_sen()
    send(sen)


if __name__ == '__main__':
    main()