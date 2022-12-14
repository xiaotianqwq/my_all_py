# -*- conding = utf-8 -*-
# @Time:2021/8/30 10:07
# @Author:宇
# @Flie:p1.py
# @Software:PyCharm

import requests
from lxml import etree
import re

url = 'http://glidedsky.com/level/web/crawler-basic-1'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84',
    'Cookie':'footprints=eyJpdiI6Imp5alJrdno3SmNFYjY5cXMxNFwvcGh3PT0iLCJ2YWx1ZSI6IkZtbG14TVQ2Q0NlamlKckFiY3o3akFqN1liN2grQ3BCa2I2RjRQV0poXC80bmcxMHp2dTVySW9nR2o2MUlWUGxCIiwibWFjIjoiY2VhZTgwY2M5ZWRjNTljMDgzOTkwYzEzNjdlYjliOTI1NGFjZDA4MTk5YTZlMTczM2JiMjZiZWM5NjlhNGY2NCJ9; Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1630287803; _ga=GA1.2.430338336.1630287803; _gid=GA1.2.857925856.1630287803; __gads=ID=1f1424bfbf4bfbc4-2230a4a238cb00ec:T=1630287805:RT=1630287805:S=ALNI_MagClLZe_d2M-s-dMR0JtPABnItpg; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IldrWEI1YUJSV0hCUG1nMVdHNGdGMWc9PSIsInZhbHVlIjoiTjVUQTFHQStVOTlkNlV4ZFVFSCt2c0ZcL3ZcL0FaalUxVHAwekM0a1Q0M1F5bm53YWJCdlAyVWhMUzA4Sm13bDhGU1BJSFZwUmNFUUxEWEU2QlZkQVhjRXhuSVdqblREb1VvN0xWZUhiZmNoeVRJXC95aERQdWtkYmkwZkY0ZlwvWmg4b0lrSHh4NWhUeUZVMFwvN0xocldsYndXT3pua2NyN3Y1SDVmTmRMbnNjdE09IiwibWFjIjoiNGZiOGZlZmYzNjBjNTA4MWQ4MjBlYmI1MTAyNjhhYTBmMmU2ODhhYjBkNTNlOTliYzViYjhhNGZjMDc3YWJhMiJ9; XSRF-TOKEN=eyJpdiI6Ik5YOHE1YUhGKzBKelR6bmR1WEVOYlE9PSIsInZhbHVlIjoiOWdEdzJkRHpVUTk0MDhnT1U3dXp0d2VOY2swaHQ4blpxUTZhS0pBeWxmVDQrV2pYaFNjclRmMGxkbnJhK1ZIYiIsIm1hYyI6ImRkYjM2Yzg2YWFkOTRmZDQ1OTU5NDU4YWMxMTM2YWIxNzYxNDU5ZWY3NDYzZjI2YTMxMDhiYzI5N2QwNTU4YjIifQ%3D%3D; glidedsky_session=eyJpdiI6IlN3R3hqQ0VHaDhnTE5iN1d4WVwvNmFnPT0iLCJ2YWx1ZSI6IllVdUxNS2xIa2syUTFnWm41MkRvYnd0Q1wvc0dMWHBkajdRVlwvWE1PNVIyRDFnbVlcL1hNUVFXYlR6MUQzQ0gzZ0UiLCJtYWMiOiI5ZThlZDRjZTQ2MWIxN2IwMzE1MDJkMzhlNmZjZTgxYmM1NGRmMDQ5YmNkNGQ4OGVkZDE3ZDQzNzRjNzA4ZjUwIn0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1630287843'
}
pape_text = requests.get(url=url,headers=headers).text
#print(pape_text)

tree = etree.HTML(pape_text)
con_list = tree.xpath('//div[@class="row"]/div/text()')
#print(con_list)

nums = 0
for con in con_list:
    con = con.replace('\\n','')
    con = con.replace(' ','')
    num = int(con)
    nums += num
print(nums)
