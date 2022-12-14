# -*- conding = utf-8 -*-
# @Time:2022/1/21 13:44
# @Author:宇
# @Flie:天气推送.py
# @Software:PyCharm
import requests

key = '9f33ab1546c446b6a36f4e0db2c9de08'
location = '泽州县'


def sing():
    # 获取城市ID
    url_ID = f'https://geoapi.qweather.com/v2/city/lookup?key={key}&location={location}'
    code_json = requests.get(url=url_ID).json()
    ID = code_json['location'][0]['id']
    print(ID)
    # 获取天气信息
    url = f'https://devapi.qweather.com/v7/weather/now?key={key}&location={ID}&lang=zh'
    code_json = requests.get(url=url).json()
    print(code_json)
    # 信息处理
    obsTime = code_json['now']['obsTime']
    temp = code_json['now']['temp']
    feelsLike = code_json['now']['feelsLike']
    text = code_json['now']['text']
    windDir = code_json['now']['windDir']
    windScale = code_json['now']['windScale']

    msg = f'''
    时间：{obsTime} 
    天气温度: {temp}℃
    体感温度：{feelsLike}℃
    天气状况：{text}
    风向：{windDir}
    风力：{windScale}级
    '''
    # 微信推送
    url_wx = 'https://sctapi.ftqq.com/SCT114686T3reNzoXK89QsVIYmz6Dx5MN2.send'
    params = {
        'title': '天气推送（微信）',
        'desp': msg
    }
    requests.post(url=url_wx,params=params)


def main():
    sing()


def main_handler(event,context):
    return main()


if __name__ == '__main__':
    main()