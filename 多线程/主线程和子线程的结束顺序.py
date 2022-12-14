# -*- conding = utf-8 -*-
# @Time:2022/1/8 16:44
# @Author:宇
# @Flie:主线程和子线程的结束顺序.py
# @Software:PyCharm
import time
import threading


def work():
    # 子线程
    for i in range(10):
        print('工作中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程
    work_thread = threading.Thread(target=work)
    # 设置守护主线程，主进程结束后自动销毁子线程，结束程序
    work_thread.daemon = True
    work_thread.start()
    # 主线程等待一秒
    time.sleep(1)
    print('主线程工作结束')