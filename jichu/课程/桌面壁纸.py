# -*- conding = utf-8 -*-
# @Time:2022/2/12 13:02
# @Author:宇
# @Flie:桌面壁纸.py
# @Software:PyCharm

import requests
from lxml import etree
import re
import json
from concurrent.futures import ThreadPoolExecutor


# 得到每一个壁纸组的url
def get_bzs_url(url):
    resp = requests.get(url=url)
    resp.encoding = 'gbk'
    et = etree.HTML(resp.text)
    bzs_url_list = et.xpath('//ul[@class="pic-list2  clearfix"]/li/a/@href')[1::]
    now_urls = []
    for bz in bzs_url_list:
        now_urls.append('https://desk.zol.com.cn/' + bz)
    return now_urls


# 得到图片地址
def get_img_scr(scr):
    imgsrc_list = []
    resp = requests.get(scr)
    et = etree.HTML(resp.text)
    str_img = et.xpath('//script/text()')[0]
    obj = re.compile(r'var deskPicArr 		= (?P<img_json>.*?);')
    result = obj.finditer(str_img)
    for iter in result:
        img_json = iter.group('img_json')
    img_dict = json.loads(img_json)
    for img_src in img_dict['list']:
        oriSize = img_src.get('oriSize')
        imgsrc = img_src.get('imgsrc')
        now_imgsrc = imgsrc.replace('##SIZE##',oriSize)
        imgsrc_list.append(now_imgsrc)
    return imgsrc_list


# 下载图片
def save(scr):
    name = scr.split('/')[-1]
    print('正在下载'+name)
    resp = requests.get(url=scr).content
    with open('桌面壁纸/'+name,'wb') as f:
        f.write(resp)
        print(name+'下载完成')


def main():
    imgs = []
    for i in range(1,10):
        if i == 1:
            url = 'https://desk.zol.com.cn/pc/'
        else:
            url = f'https://desk.zol.com.cn/pc/{i}.html'
        print(f'正在下载第{i}页')
        print('正在获取图片url')
        # 得到每一个壁纸组的url
        now_urls = get_bzs_url(url)
        # 得到图片地址
        for scr in now_urls:
            img_scrs = get_img_scr(scr)
            for img_scr in img_scrs:
                imgs.append(img_scr)
        # 下载图片
        # 创建进程池下载
        with ThreadPoolExecutor(20) as t:
            for scr in imgs:
                t.submit(save,scr)
        print(f'第{i}页下载完成')
    print('全部下载完毕！')


if __name__ == '__main__':
    main()
