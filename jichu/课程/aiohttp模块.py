# -*- conding = utf-8 -*-
# @Time:2021/8/31 10:19
# @Author:宇
# @Flie:aiohttp模块.py
# @Software:PyCharm

import asyncio
import aiohttp

urls = [
    'http://kr.shanghai-jiuxin.com/file/2021/0827/583ee2ff160f35ebb0d6ea2df709be58.jpg',
    'http://kr.shanghai-jiuxin.com/file/2021/0827/b334f1a81c761003ccd6bbd9fb6af604.jpg',
    'http://kr.shanghai-jiuxin.com/file/2021/0830/8fbbb83c0865805b0c76f54f638685ff.jpg'
]

async def download(url):
    name = url.split('/')[-1]
    print('正在下载',name)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            with open(name,'wb') as f:
                f.write(await res.content.read())
    #aiohttp.ClientSession()相当于requests
    #发送请求
    #得到图片内容
    #保存到文件

async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))
        await asyncio.wait(tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())   #把asyncio.run(main())改为这两行
    # asyncio.run(main())
