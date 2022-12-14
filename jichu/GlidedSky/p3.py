# -*- conding = utf-8 -*-
# @Time:2021/9/4 17:20
# @Author:宇
# @Flie:p3.py
# @Software:PyCharm
import time

import requests
from lxml import etree
import json
import os

os.environ['NO_PROXY'] = 'glidedsky.com'
headers = {
    'Connection': 'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
    'Cookie':'footprints=eyJpdiI6Imp5alJrdno3SmNFYjY5cXMxNFwvcGh3PT0iLCJ2YWx1ZSI6IkZtbG14TVQ2Q0NlamlKckFiY3o3akFqN1liN2grQ3BCa2I2RjRQV0poXC80bmcxMHp2dTVySW9nR2o2MUlWUGxCIiwibWFjIjoiY2VhZTgwY2M5ZWRjNTljMDgzOTkwYzEzNjdlYjliOTI1NGFjZDA4MTk5YTZlMTczM2JiMjZiZWM5NjlhNGY2NCJ9; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1630287803; _ga=GA1.2.430338336.1630287803; _gid=GA1.2.857925856.1630287803; __gads=ID=1f1424bfbf4bfbc4-2230a4a238cb00ec:T=1630287805:RT=1630287805:S=ALNI_MagClLZe_d2M-s-dMR0JtPABnItpg; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InIrRUNGem5IUFYyOE15elBGVlwvWlhnPT0iLCJ2YWx1ZSI6IkRNd0xwK3dSbmNZajB3dXJlT0dwcEJKWGhPbXVHRHRnNjRWWHVQVW9hUU4zTnhFZkkxaUQyUDIyVmUraGJKSklZMkI2MmhsTHJoaHFRaHdPNFwvakFDOXZmWW1OWWhWcUROWGUxbkc4TnpVTDBSTlZqZTR6VlJWRklIc3RcL2FtcmZ1WTlkN2NYcGMyWWtHelJJZmphS1VHVGkrNUtVYmZEOHBHTER6a0FzTzlZPSIsIm1hYyI6IjgxYTdjODdiMTM4ZWMwYjczZjhhMGU3NmEzYmY0ZmM5OGZkNTJmNjJiNmUwMDYxY2U5Njc5YzQzMmQwNGUxNmUifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IlZYajVRUEo1QjFySzRVMlhZb1JcL1FnPT0iLCJ2YWx1ZSI6InNBNkJ1RWdPbFZqY1lkaWZEUzNyalpUbnYyTUl4SEpEYWIyVExsdGt5VVVGREJhcUlNNnJSV0lZU3JzODQ2SXQiLCJtYWMiOiIzZTY1ODcwN2QxZjU5MWIyMDE1OTc2NTM1ZWJiMjM5MGMzOGRiZTM2N2M1Y2FmODI3OTAzNzU4ZDc1NDZiZDkzIn0%3D; glidedsky_session=eyJpdiI6IktFNVB3TnQzaWVFcXJ3clJZWjhkVXc9PSIsInZhbHVlIjoiMmREbzM2XC9acWcwWVZhejltTWJhc1o3MUdSRTFkWXAxSzl1aVI2a2tWQ2cwVnlDRFNDazl0TFJRRWtxWUVFWEgiLCJtYWMiOiJiNzg2YzY0ZjRjYTVlNzY1NWY0Mjc2ZjJlODVmMzE1NmE1ODgxZmExYmNkNzkxYmZkODdkY2MxMTJkY2I2Yjk3In0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1630291126'
}
all_num = []

with open('IP池.txt') as f:
    IPS = json.load(f)
    for ip in IPS:
        i = 1
        #url = 'https://www.baidu.com/'
        url = f'http://glidedsky.com/level/web/crawler-ip-block-{i}'
        pape_text = requests.get(url=url,headers=headers,proxies=ip,verify=False,timeout=5).text
        print(pape_text)
        tree = etree.HTML(pape_text)
        nums = tree.xpath('//div[@class="row"]/div/text()')
        print(nums)
        time.sleep(1)
        for num in nums:
            num = num.replace('\\n', '')
            num = num.replace(' ', '')
            num = int(num)
            all_num.append(num)
        i += 1


jg = 0
for a in all_num:
    jg += a
print(jg)