# -*- conding = utf-8 -*-
# @Time:2022/1/23 15:21
# @Author:宇
# @Flie:spa1.py
# @Software:PyCharm
import requests
import pandas as pd
requests.packages.urllib3.disable_warnings()

name = []
published_at = []
minute = []
regions = []
score = []

url = 'https://spa1.scrape.center/api/movie/?limit=100&offset=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}


def main():
    move_list = requests.get(url=url,headers=headers,verify=False).json()
    # print(move_list)
    for move in move_list['results']:
        name.append(move['name'])
        published_at.append(move['published_at'])
        minute.append(str(move['minute'])+'分钟')
        regions.append(','.join(move['regions']))
        score.append(move['score'])
    #print(len(name),len(published_at),len(minute),len(regions),len(score))

    dict = {
        'name':name,
        'published_at': published_at,
        'minute': minute,
        'regions': regions,
        'score': score
    }

    dt = pd.DataFrame(dict)
    dt.to_csv('spa1.csv')


if __name__ == '__main__':
    main()