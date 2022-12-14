# -*- conding = utf-8 -*-
# @Time:2022/2/26 11:05
# @Author:宇
# @Flie:女神的手机号.py
# @Software:PyCharm

"""
想和我出去约会吗？

请根据以下线索找出我手机号 1239098xxxx 的后 4 位，并在今晚 21:00 前短信告诉我集合地方～

##前两位数字相同
##后两位数字相同，但与前两位不同
## 4 位数字刚好是一个整数的平方
"""

for i in range(1,10):
    for j in range(10):
        if i != j:
            k = (1000 * i)+(100 * i)+(10 * j)+j
            for a in range(33,100):
                if a*a == k:
                    print(k)