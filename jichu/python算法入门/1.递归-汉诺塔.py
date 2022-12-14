# -*- coding = utf-8 -*-
# @Time:2022/7/28 14:54
# @Author:宇
# @File:1.递归-汉诺塔.py
# @Software:PyCharm


"""
n: n个圆盘
a b c 分别代表着柱子的名称
n,a,b,c  代表 n个圆盘 从 A柱子 经过 B柱子 到 C柱子
"""


def hanoi(n, a, b, c):
    # 结束条件 n = 0
    if n > 0:
        # 1. 将n-1个圆盘从 A柱子 经过 C柱子 到 B柱子
        hanoi(n - 1, a, c, b)
        # 2. 将最后一个圆盘从A移动到C
        print('%s ---> %s' % (a, c))
        # 3. 将n-1个圆盘从 B柱子 经过 A柱子 到 C柱子
        hanoi(n - 1, b, a, c)


hanoi(64, 'A', 'B', 'C')
