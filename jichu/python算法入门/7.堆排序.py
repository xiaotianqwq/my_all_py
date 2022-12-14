# -*- coding = utf-8 -*-
# @Time:2022/8/8 8:35
# @Author:宇
# @File:7.堆排序.py
# @Software:PyCharm
def sift(li, low, high):
    """
    :param li: 列表
    :param low: 堆的根节点
    :param high: 堆的最后一个人元素的位置
    :return:
    """
    i = low  # i指向堆的根节点
    j = 2 * i + 1  # j指向i的左边的孩子
    tmp = li[i]  # 把堆顶存起来
    while j <= high:  # 只要j指向的位置有数
        if j +1 <= high and li[j+1] > li[j]:  # 如果有孩子有且比较大
            j = j + 1  # 指向右孩子
        if li[j] > tmp:  # tmp较小 将j放到i的位置上
            li[i] = li[j]
            i = j  # 向下移动一层
            j = 2 * i + 1
        else:  # tmp更大 将tmp放到i的位置上
            li[i] = tmp
            break
    else:
        li[i] = tmp


def heap_sort(li):
    n = len(li)
    # 建立堆
    for i in range((n-2)//2, -1, -1):  # i 表示在建堆时的要调整的部分下表
        sift(li, i, n-1)
    for i in range(n - 1, -1, -1):  # i 堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1) # i - 1 是新high


a = [1, 9, 7, 6, 5, 4, 3, 2, 0, 8]
heap_sort(a)
print(a)
