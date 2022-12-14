# -*- coding = utf-8 -*-
# @Time:2022/4/23 17:57
# @Author:宇
# @File:课表推送_乐.py
# @Software:PyCharm
import time
import requests

Monday = [('管理幸喜系统实验@立信701教室(1-15(单))',), ('管理科学@@立信305教室(1-16)',), ('大学生心理健康教育@笃行201阶教(1-10)',)]
Tuesday = [('概率论与数理统计@立信305阶教(1-16)', '大学英语@立信604教室(1-16)'), (), ('会计学@立信303教室(1-16)',)]
Wednesday = [('公共政策分析@修德306(1-8)', '管理信息系统@立信305教室(1-16)'), ('体育基础(游泳)@坞城游泳馆(1-16)', '金融学@立信118教室(1-16)'), ()]
Thursday = [('概率论与数理统计@立信305阶教(1-16)', '大学英语@立信512教室(1-16)'), ('宏观经济学@立信305教室(9-16)',), ('管理科学实训@立信701教室(5-16)',)]
Friday = [('公共政策分析@修德306(1-8)', '经济法概论@立信206阶教'), ('马克思主义基本原理@立信101阶教(1-16)',), ()]
kbs = {
    'Monday': Monday,
    'Tuesday': Tuesday,
    'Wednesday': Wednesday,
    'Thursday': Thursday,
    'Friday': Friday
}


def now_time():
    xq, h = time.strftime('%A %H').split(' ')
    print(xq, h)
    return xq, h


def xuanke(kb, x, t):
    a = ''
    if len(kb[x]) == 0:
        return f'{t}没课哦'
    elif len(kb[x]) == 1:
        return kb[x][0] + '\n'
    else:
        for i in kb[x]:
            a += i + '\n'
        return a


def sense(xq, h):
    kb = kbs[xq]
    # 早上
    if int(h) < 8:
        x = 0
        t = '上午'
        content = xuanke(kb, x, t)
        return content

    # 中午
    if 13 < int(h) <= 14:
        x = 1
        t = '下午'
        content = xuanke(kb, x, t)
        return content

    # 下午
    if 17 <= int(h) <= 19:
        x = 2
        t = '晚上'
        content = xuanke(kb, x, t)
        return content

    else:
        return '调试'


def send(content, xq):
    token = '5f7785457f3b47a7aa9fef797f2556df'
    to = '731783f4c31d4cf9a2ee08269b61b77c'
    title = f'每日课表之{xq}'
    url = 'http://www.pushplus.plus/send'
    data = {
        'token': token,
        'title': title,
        # 'topic': '001',
        'content': content,
        'to': to
    }
    requests.post(url=url, data=data)


def main_kb():
    xq, h = now_time()
    if xq == 'Saturday' or xq == 'Sunday':
        return 0
    content = sense(xq, h)
    print(content)
    return content
    # content = content
    # send(content, xq)


if __name__ == '__main__':
    main_kb()