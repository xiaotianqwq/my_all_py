# -*- conding = utf-8 -*-
# @Time:2021/10/8 18:30
# @Author:宇
# @Flie:20000.py
# @Software:PyCharm
import time

import pyautogui
pyautogui.FAILSAFE = True
time.sleep(3)
while 1:
    rect = (0,0,1920,1018)
    jpg = pyautogui.screenshot(region=rect)
    jpg.save('jpg.png')

    result = jpg.getpixel((1082,812))
    print(result)
    if result[0] == 157:
        pyautogui.click(1086,813)
        time.sleep(4)
        pyautogui.click(736,89)
        time.sleep(2)
        pyautogui.click(1165,522)
        time.sleep(2)
        pyautogui.click(961,581)
#
#(736，89)