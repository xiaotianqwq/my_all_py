# -*- coding = utf-8 -*-
# @Time:2022/7/30 15:27
# @Author:宇
# @File:4.选择排序.py
# @Software:PyCharm

"""
遍历列表 len(li) 趟

每一趟 将无序区域中的最小值取出
      与无序区域中的第一个值交换
"""


def select_sort(li):
    for i in range(len(li)):  # i:跑第几趟
        #在无序区域中找最小值
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[i]:
                min_loc = j
        # 与无序区域中的第一个值交换
        li[i], li[min_loc] = li[min_loc], li[i]
        # print(li)


# a = [9,8,7,6,5,4,3,2,1]
# print(a)
# select_sort(a)
# print(a)