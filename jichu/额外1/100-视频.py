# -*- coding = utf-8 -*-
# @Time:2022/9/4 20:34
# @Author:宇
# @File:100-视频.py
# @Software:PyCharm
from moviepy.editor import *


def cut(clip):
    c = clip.duration - int(clip.duration)
    clip = clip.subclip(c)
    return clip


def screenshot(clip, long):
    s = f = long / 100
    i = 1
    while f <= long:
        clip.save_frame(f"视频图片/{i}.jpg", t=f)
        print(f'第{i}张图片')
        i += 1
        f += s


# clip.save_frame("视频图片/frame.png", t=0.99)  # 保存2s时刻的那1帧
if __name__ == '__main__':
    clip = VideoFileClip('./1.mp4')
    clip = cut(clip)
    long = clip.duration
    screenshot(clip, long)
    # print(clip.duration)