# -*- conding = utf-8 -*-
# @Time:2021/12/9 15:19
# @Author:宇
# @Flie:Study.py
# @Software:PyCharm
class Study():
    def __init__(self,stu_id,name,age,gander):
        self.stu_id = stu_id
        self.name = name
        self.age = age
        self.gander = gander

    def __str__(self):
        return f'{self.stu_id},{self.name},{self.age},{self.gander}'