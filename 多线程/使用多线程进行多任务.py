# -*- conding = utf-8 -*-
# @Time:2022/1/8 16:32
# @Author:宇
# @Flie:使用多线程进行多任务.py
# @Software:PyCharm
import threading
import time


def sing():
    for i in range(3):
        print('唱歌...')
        time.sleep(0.5)


def dance():
    for i in range(3):
        print('跳舞...')
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建线程对象
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)

    sing_thread.start()
    dance_thread.start()