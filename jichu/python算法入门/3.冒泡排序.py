# -*- coding = utf-8 -*-
# @Time:2022/7/30 14:46
# @Author:宇
# @File:3.冒泡排序.py
# @Software:PyCharm


# 冒泡排序
def bubble_sort(li):
    for i in range(len(li) - 1):  # i:跑第几趟
        for j in range(len(li) - 1 - i):
            # 比较j和j+1的值 进行交换
            if li[j] > li[j + 1]:  # 此处可以调整升序或降序 >为升序 <为降序
                li[j], li[j + 1] = li[j + 1], li[j]
        # print(li)


# 冒泡排序-优化
"""
增加一个标志位
记录列表是否有变化
若列表顺序无变化
说明列表顺序已经排列完成
"""


def bubble_sort_y(li):
    for i in range(len(li) - 1):  # i:跑第几趟
        exchange = False  # 每一趟结束后进行判断是否有变化
        for j in range(len(li) - 1 - i):
            # 比较j和j+1的值 进行交换
            if li[j] > li[j + 1]:  # 此处可以调整升序或降序 >为升序 <为降序
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        # print(li)
        if not exchange:
            return

# a = [3,6,8,7,4,5,2,9,1]
# print(a)
# bubble_sort_y(a)
# print(a)
