# -*- conding = utf-8 -*-
# @Time:2021/9/6 11:51
# @Author:宇
# @Flie:kuwo.py
# @Software:PyCharm
import requests,os



headers = {
    'Cookie': '_ga=GA1.2.1291419267.1630899402; _gid=GA1.2.878804585.1630899402; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1630899402,1630899462; kw_token=YPN3HHY6DN; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1630900116',
    'csrf': 'YPN3HHY6DN',
    'Referer': 'http://www.kuwo.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'
}

def get_rid_name(singer,pape):
    url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?'
    params = {
        'key': singer,
        'pn': pape,
        'rn': 30,
        'httpsStatus': '1',
        'reqId': '74162fc0-0ec5-11ec-91f7-b90d086e5b30'
    }
    dic_json = requests.get(url= url,params=params,headers=headers).json()
    for dic in dic_json['data']['list']:
        name = dic['name']
        rid = dic['rid']
        rids.append({
            'name':name,
            'rid':rid
                     })


def get_urls(rid):
    res_url = f'http://www.kuwo.cn/url?format=mp3&rid={rid}&response=url&type=convert_url3&br=128kmp3&from=web&t=1630899920953&httpsStatus=1&reqId=dc0819a1-0ec4-11ec-a1f8-ffb0f652308f'
    song_json = requests.get(url=res_url,headers=headers).json()
    #print(song_json)
    #song_urls.append(song_json['url'])
    return song_json['url']

def save (song_urls):
    for song_url in song_urls:
        name = song_url['name'] + '.mp3'
        song = requests.get(url=song_url['url'],headers=headers).content
        print('正在下载',name)
        #print(song)
        with open('music/' + singer + '/' + name,'wb') as f:
            f.write(song)

if __name__ == '__main__':
    singer = input('歌手:')
    papes = int(input('总页数:'))
    for pape in range(1,papes+1):
        print(f'正在下载第{pape}页')
        rids = []
        song_urls = []
        get_rid_name(singer,pape)
        for rid in rids:
            #get_urls(rid['rid'])
            song_urls.append({
                'name': rid['name'],
                'url': get_urls(rid['rid'])
            })
        print(song_urls)
        if not os.path.exists('music/'+singer):
            os.mkdir('music/'+singer)

        save(song_urls)
