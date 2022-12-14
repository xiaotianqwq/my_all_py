# -*- conding = utf-8 -*-
# @Time:2022/1/8 11:42
# @Author:宇
# @Flie:进程注意点（守护主进程）.py
# @Software:PyCharm
import time
import multiprocessing


def work():
    # 子进程
    for i in range(10):
        print('工作中...')
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子进程
    work_process = multiprocessing.Process(target=work)
    # 设置守护主进程，主进程结束后自动销毁子进程，结束程序
    work_process.daemon = True
    work_process.start()
    # 主进程等待一秒
    time.sleep(1)
    print('主进程工作结束')