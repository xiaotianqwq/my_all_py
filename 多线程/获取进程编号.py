# -*- conding = utf-8 -*-
# @Time:2022/1/8 11:27
# @Author:宇
# @Flie:获取进程编号.py
# @Software:PyCharm
import multiprocessing
import time
import os


def sing(num,name):
    print('唱歌的进程编号pid:',os.getpid())
    print('唱歌的父进程的进程编号pid:', os.getppid())
    for i in range(num):
        print(name)
        print('唱歌...')
        time.sleep(0.5)


def dance(num,name):
    print('跳舞的进程编号pid:', os.getpid())
    print('跳舞的父进程的进程编号pid:', os.getppid())
    for i in range(num):
        print(name)
        print('跳舞...')
        time.sleep(0.5)


if __name__ == '__main__':
    print('主进程的进程编号pid:', os.getpid())
    # 2.创建多线程对象
    #  target: 指定进程的函数名
    #  args: 使用元组的方式给指定任务传参
    #      元组的元素顺序就是函数的参数顺序
    #  kwargs:使用字典的方式给指定任务传参
    #      key名就是参数的名字
    sing_process = multiprocessing.Process(target=sing,args=(3,'xiaoming'))
    dance_process = multiprocessing.Process(target=dance,kwargs={'name':'xiaohong','num':2})
    # 3.使用多线程对象启动进程执行任务
    sing_process.start()
    dance_process.start()
