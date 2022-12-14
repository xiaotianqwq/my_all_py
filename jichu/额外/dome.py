# -*- conding = utf-8 -*-
# @Time:2021/12/13 20:24
# @Author:宇
# @Flie:dome.py
# @Software:PyCharm

def fun1(x):
    if x > 0 :
        fun1(x-1)
        print(x)


fun1(3)