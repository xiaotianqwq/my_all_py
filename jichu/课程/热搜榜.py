# -*- coding:utf-8 -*-
# @Time:2021/8/31 14:59
# @Author:宇
# @Flie:热搜榜.py
# @Software:PyCharm

import requests
from lxml import etree
from openpyxl import Workbook
import datetime

wb = Workbook()
sheet = wb.active
sheet['A1'] = '事件'
sheet['B1'] = '热度'


url = 'https://s.weibo.com/top/summary?cate=realtimehot'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
}

pape_text = requests.get(url=url,headers=headers).text
#print(pape_text)

tree = etree.HTML(pape_text)
tr_list = tree.xpath('//div[@id="pl_top_realtimehot"]//tr[@class=""]')
tr_list.pop(0)
#print(len(tr_list))

for tr in tr_list:
    title = tr.xpath('./td[@class="td-02"]/a/text()')[0]
    try:
        hot = tr.xpath('./td[@class="td-02"]/span/text()')[0]
    except:
        pass
    #print(title,hot)
    sheet.append([title,hot])

d = datetime.datetime.now()
sheet.append(['最后更新时间：',d.today()])

wb.save('热搜榜.xlsx')