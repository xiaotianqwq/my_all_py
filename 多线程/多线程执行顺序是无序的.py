# -*- conding = utf-8 -*-
# @Time:2022/1/8 16:53
# @Author:宇
# @Flie:多线程执行顺序是无序的.py
# @Software:PyCharm
import threading
import time


def task():
    time.sleep(1)
    # current_thread:获取该线程的信息
    thread = threading.current_thread()
    print(thread)


if __name__ == '__main__':
    for i in range(5):
        thread = threading.Thread(target=task)
        thread.start()


'''
结论：多线程之间执行是无序的，由CPU调度
'''