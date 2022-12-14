# -*- conding = utf-8 -*-
# @Time:2021/9/4 16:11
# @Author:宇
# @Flie:IP.py
# @Software:PyCharm

import time
import requests
from lxml import etree
import json
import threading

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
}

#得到IP
def get_IP(pape):
    url = f'https://www.kuaidaili.com/free/inha/{pape}/'
    print(f'正在爬取第{pape}页')
    pape_text = requests.get(url=url,headers=headers).text
    #print(pape_text)
    tree = etree.HTML(pape_text)
    trs = tree.xpath('//div[@id="list"]/table/tbody/tr')
    for tr in trs:
        IP = tr.xpath('./td[@data-title="IP"]/text()')[0]
        PORT = tr.xpath('./td[@data-title="PORT"]/text()')[0]
        get_IPs.append({'http':'http://' + IP + ':' +PORT})
    print(get_IPs)
    time.sleep(1)

#检查IP的有效性
def check(get_IPs):
    for ip in get_IPs:
        urls = 'https://www.baidu.com/'
        status_code = requests.get(url=urls,headers=headers,proxies=ip).status_code
        print(status_code)
        #time.sleep(1)
        if status_code == 200:
            check_IPs.append(ip)


if __name__ == '__main__':
    try:
        get_IPs = []
        check_IPs = []
        num = int(input('爬取的总页码：'))
        for pape in range(1,num+1):
            get_IP(pape)
        print('正在检查IP是否可用，请稍等')
        check(get_IPs)
        #t1 = threading.Thread(target=check,args=(get_IPs))
        print(len(check_IPs))
        print('正在保存')
        #保存
        with open('IP池.txt','w') as fp:
            json.dump(check_IPs,fp)
            print('保存完毕')
            print('共有IP数为：'+str(len(get_IPs)),'可用IP数为：'+str(len(check_IPs)))
            print('正常率：',str((len(check_IPs) / len(get_IPs))*100)+'%')
    except:
        pass