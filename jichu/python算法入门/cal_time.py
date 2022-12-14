# -*- coding = utf-8 -*-
# @Time:2022/8/3 13:40
# @Author:宇
# @File:cal_time.py
# @Software:PyCharm
import time


def cal_time(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print(t2 - t1)
        return result
    return wrapper


# def is_prime(num):
#     if num < 2:
#         return False
#     elif num == 2:
#         return True
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#         return True
#
#
# @cal_time
# def count_prime_nums(maxnum):
#     count = 0
#     for i in range(2, maxnum):
#         if is_prime(i):
#             count = count + 1
#     return count
#
#
# fgsa = count_prime_nums(5000)
# print(fgsa)
