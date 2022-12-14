# -*- coding = utf-8 -*-
# @Time:2022/7/12 10:25
# @Author:宇
# @File:抖音无水印.py
# @Software:PyCharm
import requests
import threading
import os
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
}


def getjs(id):
    url = f'https://www.douyin.com/web/api/v2/aweme/iteminfo/?item_ids={id}'
    res = requests.get(url=url, headers=headers, timeout=5).json()
    return res


def get_name_url(js):
    # 解析名字
    name = js['item_list'][0]['desc']
    # 解析url
    url = js['item_list'][0]['video']['play_addr']['url_list'][0]
    # 去水印url地址替换
    url = url.replace("/playwm/", "/play/")
    return name, url


def save(name, url):
    # # 创建视频存放的文件夹
    # if not os.path.exists('抖音视频'):
    #     os.mkdir('抖音视频')
    # id = url.split('/')[-1]
    # name = name + '_' + id + '.mp4'
    name = name.replace('\n', '') + '.mp4'
    print(name + '------正在请求......')
    res = requests.get(url=url, headers=headers).content
    # 对已经保存过的视频进行过滤
    if not os.path.exists('抖音视频\\'+'薇晓新\\' + name):
        # 保存视频
        with open('抖音视频\\'+'薇晓新\\' + name, 'wb') as f:
            f.write(res)
            print(name + '------下载完成！')
    else:
        print(name + '------已存在！')


def getid():
    wd = webdriver.Chrome('chromedriver.exe')
    print('正在获取所有视频ID......')
    ids = []
    con = 0
    wd.get('https://www.douyin.com/user/MS4wLjABAAAA9pVsrC1zqizOG84tACJX7wiU5B3FN_7YlEaoCyL8lWQ')
    # 等待2秒 关闭抖音登录窗口
    time.sleep(2)
    wd.find_elements_by_class_name('dy-account-close')[0].click()
    # 将网页下滑之最下端
    while con < 45:
        con = len(wd.find_elements_by_xpath('//ul[@class="ARNw21RN"]/li'))
        # 滑动到最底部
        js_button = 'document.documentElement.scrollTop=100000'
        # 执行js，滑动到最底部
        wd.execute_script(js_button)
        # print(con)
    # 循环取出href
    for i in wd.find_elements_by_xpath('//div[@class="mwbaK9mv"]/div[2]/ul/li/a'):
        url = i.get_attribute('href')
        id = url.split('/')[-1]
        ids.append(id)
    # print(len(ids))
    # print(ids)
    return ids


def start(id):
    # 用户输入视频ID
    # 通过抖音API获取数据包
    js = getjs(id)
    # 解析数据得到名字和地址
    name, url = get_name_url(js)
    # 对视频进行保存
    save(name, url)
    # return name,url


if __name__ == '__main__':
    # 创建视频存放的文件夹
    if not os.path.exists('抖音视频\\'+'薇晓新'):
        os.mkdir('抖音视频\\'+'薇晓新')
    try:
        ids = getid()
        for id in ids:
            start_thead = threading.Thread(target=start, args=(id,))
            start_thead.start()
    except:
        print('下载失败')
