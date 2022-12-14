# -*- coding = utf-8 -*-
# @Time:2022/7/30 13:41
# @Author:宇
# @File:2.顺序查找.py
# @Software:PyCharm
"""
顺序查找(线性查找)  从头找到尾

二分查找
"""


# 顺序查找(线性查找)
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    return -1


# 二分查找
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:  # 待选区中有值进行循环
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 查找的值在mid左边
            right = mid - 1
        else:                # li[mid] < val
            left = mid + 1
    return -1

# a = [1,2,3,4,5,67,8]
# print(binary_search(a,9))
