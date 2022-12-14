# -*- coding = utf-8 -*-
# @Time:2022/6/22 7:23
# @Author:宇
# @File:淘宝.py
# @Software:PyCharm
import pymysql
from dtk_open_platform import DtkOpenPlatform


# 连接数据库
conn = pymysql.connect(host='localhost',user='root',password='root',db='taobaoyhj')
cursor = conn.cursor()


# 请求淘宝优惠价 获取优惠劵信息（字典）
def yhjsj():
    appKey = '62b2520331e51'
    appSecret = '8e77d8187eac9f48e071a127e80143f8'
    version = 'v4.0.0'  # 当前版本号
    url = 'https://openapi.dataoke.com/api/dels/spider/list-tip-off'
    method = 'get'
    send = DtkOpenPlatform()
    data = {'appKey': appKey,
            'appSecret': appSecret,
            'version': version,
            # 'topic': '1',
            # 'type': '1'
            }
    response = send.open_platform_send(method=method, url=url, args=data, key=appSecret)
    # print(response)
    # print(type(response))
    return response


# 对字典数据处理 返回信息列表
def yhjs(yhjsj):
    # j = 0
    list_xx = yhjsj['data']['list']  # 信息列表
    print(list_xx)
    print(len(list_xx))
    return list_xx


# 查重添加副表
def chachong(itemId):
    sql = f"select 1 from yhjxx where itemIds={itemId} limit 1;"
    try:
        a = cursor.execute(sql)
        conn.commit()
    except:
        a = 1
    #print(a)
    if a == 1:
        return 1
    return 0


# sql语句执行
def sqlzx(sql):
    cursor.execute(sql)
    conn.commit()


# 向数据库提交数据
def tijiao(yhjs):
    # 清空副表
    sql1 = 'delete from yhjxxfb where 1=1;'
    sqlzx(sql1)

    for i in yhjs:
        # 取出各个值
        itemIds = "'" + i['itemIds'] + "'"
        #print(itemIds)
        content = "'" + i['content'] + "'"
        contentCopy = "'" + i['contentCopy'] + "'"
        picUrls = "'" + i['picUrls'] + "'"
        platform = "'" + i['platform'] + "'"
        urls = "'" + i['urls'] + "'"
        createTime = "'" + i['createTime'] + "'"
        updateTime = "'" + i['updateTime'] + "'"
        # 查重删除
        g = chachong(i['itemIds'])
        if g == 0:       # 数据不重复添加至副表和主表
            # 添加至副表
            sql = f"insert into yhjxxfb values({itemIds},{content},{contentCopy},{picUrls},{platform},{urls},{createTime},{updateTime});"
            sqlzx(sql)
            # 添加至主表表
            sql = f"insert into yhjxx values({itemIds},{content},{contentCopy},{picUrls},{platform},{urls},{createTime},{updateTime});"
            sqlzx(sql)
        elif g == 1:     # 数据重复 跳过
            continue
    # # 删除主表的所有数据
    # sql2 = 'delete from yhjxx where 1=1;'
    # sqlzx(sql2)
    # # 将副表的数据拷贝至主表
    # sql3 = 'insert into yhjxx select * from yhjxxfb;'
    # sqlzx(sql3)


# 查数据
def cha():
    sj_list = []
    sql = 'select * from yhjxxfb'
    sqlzx(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        platform = row[4]
        content = row[1]
        picUrls = row[3]
        sj_list.append((picUrls,content,platform))
    # print(sj_list)
    return sj_list


# 删除某条数据
def delsql(itemId):
    sql = f"delete from yhjxx where itemIds={itemId}"
    cursor.execute(sql)
    conn.commit()
    print('删除'+itemId)


# 断开与数据库的连接
def close():
    cursor.close()
    conn.close()


# 发送数据
def send(sj_list):
    print(sj_list)
    for i in sj_list:
        picUrls = i[0]
        content = i[1]
        platform = i[2]
        cons = platform + '\n' + '[pic=' + picUrls + ']' + '\n' + content
        print(cons)
        print('\n', end='')


if __name__ == '__main__':
    # 请求淘宝优惠价 获取优惠劵信息（字典）
    yhjsj = yhjsj()
    # 对字典数据处理 返回信息列表
    yhjs = yhjs(yhjsj)
    # 向数据库提交数据
    tijiao(yhjs)
    # 查数据
    sj_list = cha()
    send(sj_list)
    # 断开与数据库的连接
    close()