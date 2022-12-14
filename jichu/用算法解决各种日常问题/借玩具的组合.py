# -*- conding = utf-8 -*-
# @Time:2022/2/27 10:35
# @Author:宇
# @Flie:借玩具的组合.py
# @Software:PyCharm
"""
这讲咱们来解决一个借玩具问题，小由鱼到手了 5 个新玩具，准备借给 3 位鱼油，并且一人只能借一个玩具。
请问：
有多少种不同的借法？
"""

"""
a,b,c三人
0，1，2，3，4为五个玩具
"""
flag = 0
for a in range(5):
    for b in range(5):
        if a != b:
            for c in range(5):
                if a != c and b != c:
                    flag += 1
                    print(f'A:{a}  B:{b}  C:{c}')

print(f'总共有{flag}种方案')

a = []
a.sort(reverse=False)