# -*- conding = utf-8 -*-
# @Time:2021/11/29 21:45
# @Author:宇
# @Flie:搬家具.py
# @Software:PyCharm
'''
类名： 家具 Jiaju
属性：
    类型 self.leixing = leixing
    占用面积 self.mianji = mianji
方法：
    输出信息 __str__


类名： 房子 fangzi
属性：
    地址 self.dizhi = dizhi
    占用面积 self.mianji = mianji
    家具列表 self.jiaju_list = []
方法：
    增加家具 add()
        判断房间面积，家具面积
    输出信息 __str__
'''


class Jiaju():
    def __init__(self,leixing,mianji):
        self.leixing = leixing
        self.mianji = mianji

    def __str__(self):
        return f'<{self.leixing}>占地面积为<{self.mianji}>'


class Fanzi():
    def __init__(self,dizhi,mianji):
        self.dizhi = dizhi
        self.mianji = mianji
        self.mianjis = mianji
        self.jiaju_list = []

    def add(self,jiaju):
        if jiaju.mianji < self.mianji:
            self.jiaju_list.append(jiaju)
            self.mianjis -= jiaju.mianji
            print(f'成功添加<{jiaju.leixing}>')
        else:
            print(f'<{jiaju.leixing}>添加失败')

    def __str__(self):
        bft =[bot.leixing for bot in self.jiaju_list]
        if bft:
            return f'房子的位于<{self.dizhi}>,占地面积为<{self.mianji}>,剩余面积为<{self.mianjis}>,房子的家具有{",".join(bft)}'
        else:
            return f'房子的位于<{self.dizhi}>,占地面积为<{self.mianji}>,剩余面积为<{self.mianjis}>,房子还未添加家具'


zhuozi = Jiaju('桌子',10)
print(zhuozi)
fz = Fanzi('...',100)
fz.add(zhuozi)
print(fz)