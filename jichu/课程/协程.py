# -*- conding = utf-8 -*-
# @Time:2021/8/31 9:27
# @Author:宇
# @Flie:协程.py
# @Software:PyCharm
import asyncio
# async def fun():
#     print('fun')
#
# if __name__ == '__main__':
#     g = fun()        #得到协程对象
#     asyncio.run(g)   #协程程序的运行需要asyncio模块
import time


# async def fun1():
#     print('1')
#     #time.sleep(3)  #出现同步操作，异步中断
#     await asyncio.sleep(3)
#     print('1')
#
# async def fun2():
#     print('2')
#     #time.sleep(2)
#     await asyncio.sleep(2)
#     print('2')
#
# async def fun3():
#     print('3')
#     #time.sleep(4)
#     await asyncio.sleep(4)
#     print('3')
#
# if __name__ == '__main__':
#     f1 = fun1()
#     f2 = fun2()
#     f3 = fun3()
#     tasks = [f1,f2,f3]
#     asyncio.run(asyncio.wait(tasks))


# async def fun1():
#     print('1')
#     #time.sleep(3)  #出现同步操作，异步中断
#     await asyncio.sleep(3)
#     print('1')
#
# async def fun2():
#     print('2')
#     #time.sleep(2)
#     await asyncio.sleep(2)
#     print('2')
#
# async def fun3():
#     print('3')
#     #time.sleep(4)
#     await asyncio.sleep(4)
#     print('3')
#
# async def main():
#     tasks = [fun1(),fun2(),fun3()]
#     await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     asyncio.run(main())

async def download(url):
    print('开始下载......',url)
    await asyncio.sleep(2)
    print('下载完成',url)

async def main():
    urls = [
        '1',
        '2',
        '3'
    ]
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url))) #转换成tasks对象
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())