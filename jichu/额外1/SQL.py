# -*- coding = utf-8 -*-
# @Time:2022/6/1 19:17
# @Author:宇
# @File:SQL.py
# @Software:PyCharm
import random

import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='stulx1',
    autocommit=True,
    charset='utf8'
)

cor = conn.cursor()
for i in range(10):
    id = str(random.randint(10000,20000))
    print('id '+id)
    pwd = str(random.randint(10000, 20000))
    print('pwd '+pwd)
    money = str(random.randint(10000, 20000))
    print('money '+money)

    insert_sqli = "insert into bank value ('%s','%s','%s')" % (id, pwd, money)
    cor.execute(insert_sqli)
    print("111111")