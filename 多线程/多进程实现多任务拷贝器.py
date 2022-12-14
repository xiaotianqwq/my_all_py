# -*- conding = utf-8 -*-
# @Time:2022/1/8 15:51
# @Author:宇
# @Flie:多线程转换器.py
# @Software:PyCharm
import os
import multiprocessing


def copy_file(file_name, source_dir, dest_dir):
    # 1.拼接源目标路径和目标文件路径
    source_path = source_dir + '\\' + file_name
    dest_path = dest_dir + '\\' + file_name
    # 2.打开源文件和目标文件
    with open(source_path,'rb') as source_file:
        with open(dest_path,'wb') as dest_file:
            # 3.循环文件内容依次拷贝
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    # 1.定义源目标路径和目标文件路径
    source_dir = r'D:\123'
    dest_dir = r'D:\1234'
    # 2.创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except Exception:
        print('文件夹存在')
    # 3.读取源文件夹的文件列表
    file_list = os.listdir(source_dir)
    # 4.遍历文件列表进行拷贝
    for file_name in file_list:
        # copy_file(file_name,source_dir,dest_dir)
        # 5.使用多进程进行拷贝
        copy_process = multiprocessing.Process(target=copy_file, args=(file_name, source_dir, dest_dir))
        copy_process.start()
