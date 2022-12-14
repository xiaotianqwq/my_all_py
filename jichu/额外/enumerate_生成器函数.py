# -*- coding = utf-8 -*-
# @Time:2022/4/12 18:09
# @Author:宇
# @File:enumerate_生成器函数.py
# @Software:PyCharm

def my_enumerate(list1):
    for i in range(len(list1)):
        yield i, list1[i]


def my_zip(list1, list2):
    if len(list1) > len(list2):
        f = len(list2)
    else:
        f = len(list1)

    for i in range(f):
        yield list1[i], list2[i]


a = ['fe', 1, 8, 'r']
b = ['yg', 7, 5, 'oi', 8]
for i in my_zip(b, a):
    print(i)
