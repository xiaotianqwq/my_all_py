# -*- coding = utf-8 -*-
# @Time:2022/7/31 13:41
# @Author:宇
# @File:5.插入排序.py
# @Software:PyCharm


def insert_sort(li):
    for i in range(1, len(li)):  # i表示摸到牌的下标
        tmp = li[i]  # 摸到的牌
        j = i - 1  # 手里到的牌
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp


# a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(a)
# insert_sort(a)
# print(a)
