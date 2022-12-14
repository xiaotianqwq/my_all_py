# -*- conding = utf-8 -*-
# @Time:2022/1/22 11:20
# @Author:宇
# @Flie:ssr1.py
# @Software:PyCharm
import requests
from lxml import etree
import pandas as pd
requests.packages.urllib3.disable_warnings()


names = []
locations = []
time_longs = []
ages = []
sites = []
scroes = []
summarys = []


def main():
    for i in range(1, 11):
        print(f'第{i}页')
        url_page = f'https://ssr1.scrape.center/page/{i}'
        pape_list = requests.get(url_page,verify=False).text
        # print(pape_list)
        html = etree.HTML(pape_list)

        # names
        name_move_list = html.xpath('//div/div/div[2]/a/h2/text()')
        # print(name_move_list)
        for name in name_move_list:
            names.append(name)
        # print(len(names))

        # locations
        location_move_list = html.xpath('//div/div/div/div[2]/div[2]/span[1]/text()')
        # print(location_move_list)
        for l in location_move_list:
            locations.append(l)
        # print(len(locations))

        # time_longs
        time_move_list = html.xpath('//div/div/div/div[2]/div[2]/span[3]/text()')
        # print(time_move_list)
        for t in time_move_list:
            time_longs.append(t)
        # print(len(time_longs))

        # scroes
        scores_move_list = html.xpath('//p[@class="score m-t-md m-b-n-sm"]/text()')
        for sc in scores_move_list:
            scroes.append(sc)

        # sites
        site_move_list = html.xpath('//div[@class="el-card item m-t is-hover-shadow"]/div/div/div[1]/a/@href')
        # print(site_move_list)
        for s in site_move_list:
            site = 'https://ssr1.scrape.center' + s
            sites.append(site)
            move_res = requests.get(site,verify=False).text
            html_move = etree.HTML(move_res)
            summary = html_move.xpath('//div[@class="drama"]/p/text()')[0].strip()
            summarys.append(summary)
        # print(len(sites))

        # 字典
        dict = {
            'name': names,
            'location': locations,
            'duration': time_longs,
            'summary': summarys,
            'site': sites,
            'scroes': scroes
        }
        df = pd.DataFrame(dict)
        df.to_csv('ssr2.csv')


if __name__ == '__main__':
    main()
