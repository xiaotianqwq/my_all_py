# -*- coding = utf-8 -*-
# @Time:2022/8/10 14:06
# @Author:宇
# @File:8.heapq.py
# @Software:PyCharm
import heapq
import random

li = list(range(100))
random.shuffle(li)

print(li)

heapq.heapify(li)  # 建立堆（小根堆）
# print(li)
# heapq.heappop(li)
# print(li)
n = len(li)
for i in range(n):
    # heapq.heappop(li)  弹出一个数据
    print(heapq.heappop(li), end=',')