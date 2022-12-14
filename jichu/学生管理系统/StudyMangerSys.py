# -*- conding = utf-8 -*-
# @Time:2021/12/9 15:19
# @Author:宇
# @Flie:StudyMangerSys.py
# @Software:PyCharm
import Study


class StudyMangerSys(object):
    def __init__(self):
        self.stu_dic = {}

    @staticmethod
    def __show_maue(self):
        print('1.增加学生信息')
        print('2.删除学生信息')
        print('3.查找学生信息')
        print('4.修改学生信息')
        print('5.显示所有学生信息')
        print('6.读取学生信息')
        print('7.退出系统')

    # 增加学生信息
    def __add_stu(self):
        # 学生信息
        stu_id = input('输入学号：')
        if stu_id in self.stu_dic:
            print('该学生已存在，请勿重复添加')
            return
        name = input('输入姓名：')
        age = input('输入年龄：')
        gander = input('输入性别：')
        # 实例化对象
        stu = Study.Study(stu_id,name,age,gander)
        # 加入所有学生字典
        self.stu_dic[stu_id] = stu

    # 删除学生信息
    def __pop_stu(self):
        stu_id = input('输入所删除的学生学号：')
        if not stu_id in self.stu_dic:
            print('学生不存在')
            return
        self.stu_dic.pop(stu_id)
        print(f'{stu_id}已删除')

    # 查找学生信息
    def __check_stu(self):
        stu_id = input('输入查询学生的学号：')
        print(self.stu_dic[stu_id])

    # 修改学生信息
    def __change_stu(self):
        stu_id = input('输入修改学生的学号：')
        name = input('输入姓名：')
        age = input('输入年龄：')
        gander = input('输入性别：')
        stu = Study.Study(stu_id, name, age, gander)
        self.stu_dic[stu_id] = stu

    # 显示所有学生信息
    def __show_all_stu(self):
        if self.stu_dic == {}:
            print('暂无学生信息')
        for stu in self.stu_dic.values():
            print(stu)

    # 保存信息
    def __save(self):
        f = open('study.txt','w',encoding='utf-8')
        for stu in self.stu_dic.values():
            f.write(str(stu) + '\n')
        f.close()

    # 读取信息
    def __load_info(self):
        try:
            f = open('study.txt','r',encoding='utf-8')
            but_list = f.readlines()
            for but in but_list:
                but = but.strip()
                info_list = but.split(',')
                # 创建学生对象
                stu = Study.Study(*info_list)
                stu_id = but[0]
                self.stu_dic[stu_id] = stu
            f.close()
        except Exception:
            pass

    def start(self):
        while True:
            self.show_maue(self)
            obt = input('选择功能键：')
            if obt == '1':
                # print('1.增加学生信息')
                self.add_stu()
            elif obt == '2':
                # print('2.删除学生信息')
                self.pop_stu()
            elif obt == '3':
                # print('3.查找学生信息')
                self.check_stu()
            elif obt == '4':
                # print('4.修改学生信息')
                self.change_stu()
            elif obt == '5':
                # print('5.显示所有学生信息')
                self.show_all_stu()
            elif obt == '6':
                # print('6.读取学生信息')
                self.load_info()
            elif obt == '7':
                # print('7.退出系统')
                self.save()
                print('已退出')
                return

            input('------回车键继续------')
