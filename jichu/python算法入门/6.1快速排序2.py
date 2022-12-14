# -*- coding = utf-8 -*-
# @Time:2022/8/3 14:03
# @Author:宇
# @File:6.1快速排序2.py
# @Software:PyCharm
from cal_time import *


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找出比tmp小的数
            right -= 1  # 向左走一步
        li[left] = li[right]  # 将右边的值写到左边空位上
        while left < right and li[left] <= tmp:  # 从左边找出比tmp大的数
            left += 1  # 向右走一步
        li[right] = li[left]  # 将左边的值写到右边空位上
    li[left] = tmp  # tmp归位
    return left


def _quick_sort(li, left, right):
    if left < right:  # 最少有两个元素
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


a = [1, 9, 7, 6, 5, 4, 3, 2, 8]
quick_sort(a)
print(a)
