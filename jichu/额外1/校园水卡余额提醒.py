# -*- coding = utf-8 -*-
# @Time:2022/11/12 10:20
# @Author:宇
# @File:校园水卡余额提醒.py
# @Software:PyCharm
import requests
import datetime

headers = {
    'User-Agent': 'okhttp / 4.2.2'
}


def get_money():
    url = 'https://v3-api.china-qzxy.cn/account/wallet/money'
    data = {
        'projectId': '940',
        'telephone': '18835668071',
        'userId': '10042853',
        'accountId': '1863',
        'ersion': '6.3.3',
        'phoneSystem': 'android',
        'loginCode': '2de992c0793b4b57481eccd042509a19',
        'telPhone': '18835668071'
    }
    res = requests.get(url=url, params=data, headers=headers).json()
    # print(res['data']['money'])
    return res['data']['money']


def get_data():
    url = 'https://v3-api.china-qzxy.cn/order/query/account/bill/list'
    now = datetime.date.today()
    data = {
        'projectId': '940',
        'billRequestType': '0',
        'month': str(now.year)+'-'+str(now.month),
        'telephone': '18835668071',
        'userId': '10042853',
        'accountId': '1863',
        'ersion': '6.3.3',
        'phoneSystem': 'android',
        'loginCode': '2de992c0793b4b57481eccd042509a19',
        'telPhone': '18835668071'
    }
    res = requests.get(url=url, params=data, headers=headers).json()

    now_sortTimestamp = str(res['data'][0]['sortTimestamp'])
    # print(now_sortTimestamp)
    flag = chack_sortTimestamp(now_sortTimestamp)

    if flag:
        use_time = res['data'][0]['consumeBillDTO']['dealDate']
        consumeMoney = res['data'][0]['consumeBillDTO']['consumeMoney']
        description = res['data'][0]['consumeBillDTO']['description']
        money = get_money()
        return use_time, consumeMoney, description, money
    else:
        return None, None, None, None


def save_sortTimestamp(sortTimestamp):
    with open('sortTimestamp.txt', 'w') as f:
        f.write(sortTimestamp)


def chack_sortTimestamp(now_sortTimestamp):
    with open('sortTimestamp.txt', 'r') as f:
        f.seek(0)
        data = f.read()
    if data == '' or data != now_sortTimestamp:
        save_sortTimestamp(now_sortTimestamp)
        flag = 1
    elif data == now_sortTimestamp:
        flag = 0
    return flag


def send(sense):
    key = '9a753457490a93cfa9d17d4b5a1656a1'
    url = f'https://qmsg.zendee.cn:443/send/{key}'
    data = {
        'msg':sense,
        'qq':'3316578998'
    }
    requests.post(url=url,data=data)


if __name__ == '__main__':
    stop_date = datetime.date(2022,12,10)
    now = datetime.date.today()
    if now < stop_date:
        use_time, consumeMoney, description, money = get_data()
        print(money)

        # if int(money) <= 5:
        #     sense_money = f'余额仅剩{money}元，请尽快充值！！！'
        #     for i in range(3):
        #         send(sense_money)

        if use_time is not None:
            sense = f'趣智校园\n最近一次使用时间:{use_time}\n花费:{consumeMoney}元\n剩余余额:{money}元\n使用设备:{description}'
            # print(sense)
            send(sense)
        # print(now)
    # # money = get_money()
    # sortTimestamp = get_now_sortTimestamp()
    # save_sortTimestamp(sortTimestamp)
    # chack_sortTimestamp()
    # use_time, consumeMoney, description, money = get_data()
    # if money <= 5:
    #     sense_money = f'余额仅剩{money}元，请尽快充值！！！'
    #     for i in range(3):
    #         send(sense_money)
    # if use_time is not None:
    #     sense = f'趣智校园\n最近一次使用时间:{use_time}\n花费:{consumeMoney}元\n剩余余额:{money}元\n使用设备:{description}'
    #     print(sense)
    #     send(sense)

