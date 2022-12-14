# -*- conding = utf-8 -*-
# @Time:2022/2/26 10:40
# @Author:宇
# @Flie:百钱百鸡.py
# @Software:PyCharm

"""
已知：
  一只公鸡5元，一只母鸡3元，3只小鸡1元
请问：
  用100元买100知鸡，公鸡，母鸡，小鸡各买几只？
"""

gongji = 5
muji = 3

for a in range(20):
    for b in range(33):
        if a*gongji + b*muji +(100 - (a + b))*(1 / 3) == 100:
            print('公鸡买'+str(a),'母鸡鸡买'+str(b),'小鸡买'+str((100 - (a + b))))