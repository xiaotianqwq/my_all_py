# -*- conding = utf-8 -*-
# @Time:2022/1/8 10:20
# @Author:宇
# @Flie:多线程例子.py
# @Software:PyCharm

# 1.导入多线程包
# 2.创建多线程对象
# 3.使用多线程对象启动进程执行任务
import multiprocessing
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
    sing_process = multiprocessing.Process(target=sing,args=(3,'xiaoming'))
    dance_process = multiprocessing.Process(target=dance,kwargs={'name':'xiaohong','num':2})
    # 3.使用多线程对象启动进程执行任务
    sing_process.start()
    dance_process.start()
