# -*- coding = utf-8 -*-
# @Time:2022/4/17 10:05
# @Author:宇
# @File:1111.py
# @Software:PyCharm
import requests
import os
import multiprocessing
from lxml import etree

headers = {
    'Referer': 'https://www.mmlme.com/jp',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}


# 获取图组链接
def get_zu_urls(pepa):
    zu_title_urls = {}
    url = f'https://www.mmlme.com/jp/page/{pepa}'
    res = requests.get(url=url,headers=headers).text
    tree = etree.HTML(res)
    title = tree.xpath('//div[@class="posts-row ajaxpager"]/posts/div[2]/h2/a/text()')
    # print(len(title))
    urls = tree.xpath('//div[@class="posts-row ajaxpager"]/posts/div[2]/h2/a/@href')
    # print(len(urls))
    for i in range(12):
        zu_title_urls[title[i]] = urls[i]
    # print(zu_title_urls)
    return zu_title_urls


# 得到图片url
def get_urls(urls):
    res = requests.get(url=urls,headers=headers).text
    tree = etree.HTML(res)
    urls_list = tree.xpath('//ul/li/figure/a/@box-img')
    # print(urls_list)
    return urls_list


def save(name, urls_list):
    a = 1
    for i in urls_list:
        res = requests.get(url=i,headers=headers).content
        # print(a)
        with open('图库/' + name + '/' + str(a) + '.jpg', 'wb') as f:
            f.write(res)
        a += 1
    print(name+'下载完成！！！！！！！')


def main():
    for pepa in range(1, 6):
        # 获取图组链接
        print(f'正在下载第{pepa}页......')
        zu_title_urls = get_zu_urls(pepa)
        # 创建文件夹
        if not os.path.exists('图库'):
            os.mkdir('图库')

        for i in zu_title_urls.items():
            if not os.path.exists('图库/'+i[0]):
                os.mkdir('图库/'+i[0])
            print(i[0]+'......')
            # 得到图片url
            urls_list = get_urls(i[1])
            # save(i[0],urls_list)
            # 多线程
            save_process = multiprocessing.Process(target=save, args=(i[0],urls_list))
            save_process.start()
            # a = 1
            # for img in res(urls):
            #     # print(a)
            #     with open('图库/'+i[0]+'/'+str(a)+'.jpg', 'wb') as f:
            #         f.write(img)
            #     a += 1
        print(f'第{pepa}页' + '下载完成！！！！！！！')


if __name__ == '__main__':
    main()