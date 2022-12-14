# -*- conding = utf-8 -*-
# @Time:2021/10/23 15:36
# @Author:宇
# @Flie:we learn.py
# @Software:PyCharm
import time

from selenium import webdriver
from time import sleep

#账号密码
#namename = input('账号:')
#namepass = input('密码：')
#x = int(input('第几单元：'))

browser = webdriver.Edge(executable_path ="./msedgedriver.exe")
browser.get("https://course.sflep.com/index.aspx")

#登录
login = browser.find_element_by_id("aLogin")
sleep(2)
login.click()
login_name = browser.find_element_by_id('username')
login_pass = browser.find_element_by_id('password')
login_name.send_keys('18835668071')
login_pass.send_keys('cgywn335')
denglu = browser.find_element_by_name('submit')
denglu.click()
#进入课程
jiaocheng = browser.find_element_by_class_name('thumbnail')
jiaocheng.click()

def start1():
    ux = browser.find_elements_by_class_name('collapsed')[1]
    ux.click()
    learn_start = browser.find_elements_by_xpath()

