# -*- conding = utf-8 -*-
# @Time:2021/11/29 15:06
# @Author:宇
# @Flie:potato.py
# @Software:PyCharm
'''
类名：地瓜类 Potato
属性:
    状态 status = '生的'
    烧烤总时间 all_time = 0
方法：
    可以进行烧烤
    def cook(self,烧烤的时间):
        计算烧烤时间
        更改地瓜状态
    输出属性 __str__
    初始属性__init__
'''


class Potato():
    def __init__(self):
        self.statua = '生的'
        self.all_time = 0
        self.name_list = []

    def cook(self, time):
        self.all_time += time
        if self.all_time < 3:
            self.statua = '生的'
        elif self.all_time < 6:
            self.statua = '半生不熟的'
        elif self.all_time < 8:
            self.statua = '熟的'
        else:
            self.statua = '烤糊了'

    def add(self, name):
        self.name_list.append(name)

    def __str__(self):
        but = ','.join(self.name_list)
        if self.name_list:
            return f'地瓜的状态是<{self.statua}>,烤地瓜的总时长是<{self.all_time}>,加入的调料有：{but}'
        else:
            return f'地瓜的状态是<{self.statua}>,烤地瓜的总时长是<{self.all_time}>,还未加入任何调料'


potato = Potato()
print(potato)
potato.add('孜然')
potato.cook(4)
potato.add('辣椒')
potato.cook(3)
print(potato)
