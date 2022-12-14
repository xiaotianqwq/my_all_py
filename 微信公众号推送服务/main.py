# -*- coding = utf-8 -*-
# @Time:2022/8/23 18:06
# @Author:宇
# @File:main.py
# @Software:PyCharm
import requests
import json
import datetime
from V课表推送_乐 import *

# 和风天气的key
key = '9f33ab1546c446b6a36f4e0db2c9de08'

# 每日一句
app_id = 'ygsxepmrexfnoxsq'
app_secret = 'eUNYNUlHK2w5amFUOU1LVEl3amQ2Zz09'

def get_city_id(name):
    url = f'https://geoapi.qweather.com/v2/city/lookup?key={key}&location={name}'
    res = requests.get(url=url).json()
    id = res["location"][0]["id"]
    # print(res)
    # print(id)
    return id


def get_access_token(appid, secret):
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}'
    res = requests.get(url=url).json()
    access_token = res["access_token"]
    return access_token


# 天气信息
def get_weather(city_name):
    weather_dic = {}
    id = get_city_id(city_name)
    url = f'https://devapi.qweather.com/v7/weather/now?key={key}&location={id}'
    res = requests.get(url=url).json()
    # print(res)

    weather_dic['city'] = city_name  # 当前城市
    weather_dic['obsTime'] = res['now']['obsTime'].split('T')[0]  # 时间
    weather_dic['text'] = res['now']['text']  # 天气
    weather_dic['temp'] = res['now']['temp'] + '℃'  # 温度
    weather_dic['feelsLike'] = res['now']['feelsLike'] + '℃'   # 体感温度
    weather_dic['windScale'] = res['now']['windScale'] + '级'  # 风力等级

    return weather_dic


# 恋爱天数
def get_love_date():
    t1 = datetime.date(2021, 3, 10)
    t2 = datetime.date.today()
    return (t2 - t1).days


# 每日一句
def get_sense():
    url = f'https://www.mxnzp.com/api/daily_word/recommend?count=1&app_id={app_id}&app_secret={app_secret}'
    res = requests.get(url=url).json()
    # print(res['data'][0]['content'])
    return res['data'][0]['content']


# 生日
def get_birthday():
    today = datetime.date.today()
    birthday_year = today.year
    birthday = datetime.date(birthday_year, 9, 19)
    if today < birthday:
        birthday_time = (birthday - today).days
    elif today > birthday:
        birthday_time = (birthday - today).days + 365
    else:
        birthday_time = 0
    return birthday_time


def send(weather_dic, love_date, sense, birth, kebiao):
    appid = 'wxd8d8636ff4e81f41'
    secret = '217d51059b3c19ff7a6dc0a9e5893f18'
    #touser = ['oFus16nqz5KLvEzln6ujMZly3TmM', 'oFus16prsralvHAx9DwVVxTpCYyI']
    touser = 'oFus16prsralvHAx9DwVVxTpCYyI'
    access_token = get_access_token(appid, secret)
    url = f'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_token}'

    data = {
        'touser': touser,
        'template_id': 'NkdM7l_fgO41-s2vkmRXe5XtwAafeMoWbja7Ghr_Cto',
        'appid': 'wxd8d8636ff4e81f41',
        'data': {
            'city': {
                'value': weather_dic['city']  # 当前城市
            },
            'obsTime': {
                'value': weather_dic['obsTime'],  # 时间
                'color': '#67b0ca'
            },
            'text': {
                'value': weather_dic['text'],  # 天气
                'color': '#67b0ca'
            },
            'temp': {
                'value': weather_dic['temp'],  # 温度
                'color': '#15182f'
            },
            'feelsLike': {
                'value': weather_dic['feelsLike'],  # 体感温度
                'color': '#c77764'
            },
            'windScale': {
                'value': weather_dic['windScale']  # 风力等级
            },
            'love_date': {
                'value': str(love_date),  # 恋爱天数
                'color': '#8f3557'
            },
            'sense': {
                'value': sense,  # 每日一句
                'color': '#d980a1'
            },
            'birth': {
                'value': birth,  # 生日
                'color': '#d0a155'
            },
            'kebiao': {
                'value': kebiao  # 课表
            }
        }
    }
    data_json = json.dumps(data)
    A = requests.post(url=url, data=data_json).json()
    print(A)


def main():
    # 获取城市天气
    city_name = '太原'
    weather_dic = get_weather(city_name)   # 天气信息
    love_date = get_love_date()    # 恋爱天数
    #print(weather_dic)
    sense = get_sense()  # 每日一句
    birthday_time = get_birthday()
    kebiao = main_kb()
    # if birthday == 0:
    #     birth = '今天是你生日哦！'
    # else:
    #     birth = f'距离你生日还有{birthday}天'
    send(weather_dic, love_date, sense, birthday_time, kebiao)  # 发送


if __name__ == '__main__':
    main()