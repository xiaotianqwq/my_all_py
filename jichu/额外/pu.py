# -*- conding = utf-8 -*-
# @Time:2021/11/23 9:08
# @Author:宇
# @Flie:pu.py
# @Software:PyCharm

f = open('D://胡桃摇.txt','r')
f1 = open('D://胡桃摇1.txt','w')
#print(f.read())

for sense in f.readlines():
    #print(sense)
    for i in sense:
        print(i)
        if i == '-':
            f1.write('Delay 220')
            f1.write('\n')
        elif i == '=':
            f1.write('Delay 110')
            f1.write('\n')
        elif i == '\n':
            f1.write('')
        else:
            f1.write(f'KeyPress "{i}",1')
            f1.write('\n')

f.close()
f1.close()