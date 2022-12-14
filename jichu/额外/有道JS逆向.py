# -*- coding = utf-8 -*-
# @Time:2022/4/12 19:14
# @Author:宇
# @File:有道JS逆向.py
# @Software:PyCharm

# i: cat
# from: AUTO
# to: AUTO
# smartresult: dict
# client: fanyideskweb
# salt: 16497619914778   。。。。
# sign: 35e8489334d48ed118cd9f3b246fd9cd   。。。。
# lts: 1649761991477  。。。。
# bv: 803d4a8f2036921cf486753934c3ae8a
# doctype: json
# version: 2.1
# keyfrom: fanyi.web
# action: FY_BY_REALTlME

import time
import requests
import random
from hashlib import md5

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '244',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=723909181.2194293; OUTFOX_SEARCH_USER_ID="1775340763@10.108.160.131"; _ga=GA1.2.1885958751.1641267053; P_INFO=null; JSESSIONID=abc1pQo56vyiG-586DDay; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; fanyi-ad-id=305426; fanyi-ad-closed=1; ___rl__test__cookies=1649761991475',
    'Host': 'fanyi.youdao.com',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

word = input('输入单词：')
r = str(int((time.time()) * 1000))
i = r + str(random.randint(0,9))

# md5加密 ("fanyideskweb" + 翻译的单词 + i + "Ygy_4c=r#e#4EX^NUGUc5")
md = md5()
str1 = "fanyideskweb" + word + i + "Ygy_4c=r#e#4EX^NUGUc5"
md.update(str1.encode())
mds = md.hexdigest()

data = {
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': i,
    'sign': mds,
    'lts': r,
    'bv': '803d4a8f2036921cf486753934c3ae8a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}

res = requests.post(url=url, data=data, headers=headers).json()
con1 = '基础词义' + res['translateResult'][0][0]['tgt'] + '\n'
con2 = res['smartResult']['entries'][1] + res['smartResult']['entries'][2]
print(con1+con2)
