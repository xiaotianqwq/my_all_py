# -*- coding = utf-8 -*-
# @Time:2022/6/20 19:50
# @Author:宇
# @File:注册.py
# @Software:PyCharm
import requests
import threading
import os
import time
from selenium import webdriver

wd = webdriver.Chrome('chromedriver.exe')
wd.get('https://www.yebaojiasu.com/act/million_quiz/?inviter=uu8OO9gjaxXCWMZQrcbF1g==')
time.sleep(2)
wd.find_elements_by_xpath('//*[@id="bg"]/div/div[17]/div/div[10]')[0].click()
