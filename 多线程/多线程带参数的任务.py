# -*- conding = utf-8 -*-
# @Time:2022/1/8 16:39
# @Author:宇
# @Flie:多线程带参数的任务.py
# @Software:PyCharm
import threading
import time


def sing(num,name):
    for i in range(num):
        print(name)
        print('唱歌...')
        time.sleep(0.5)


def dance(num,name):
    for i in range(num):
        print(name)
        print('跳舞...')
        time.sleep(0.5)


if __name__ == '__main__':
    # 2.创建多线程对象
    #  target: 指定进程的函数名
    #  args: 使用元组的方式给指定任务传参
    #      元组的元素顺序就是函数的参数顺序
    #  kwargs:使用字典的方式给指定任务传参
    #      key名就是参数的名字
    sing_thread = threading.Thread(target=sing,args=(3,'xiaoming'))
    dance_thread = threading.Thread(target=dance,kwargs={'name':'xiaohong','num':2})
    # 3.使用多线程对象启动进程执行任务
    sing_thread.start()
    dance_thread.start()
