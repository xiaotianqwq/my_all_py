# -*- coding = utf-8 -*-
# @Time:2022/8/3 12:46
# @Author:宇
# @File:6.快速排序.py
# @Software:PyCharm

def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找出比tmp小的数
            right -= 1      # 向左走一步
        li[left] = li[right]  # 将右边的值写到左边空位上
        while left < right and li[left] <= tmp:  # 从左边找出比tmp大的数
            left += 1       # 向右走一步
        li[right] = li[left]  # 将左边的值写到右边空位上
    li[left] = tmp  # tmp归位
    return left


def quick_sort(li, left, right):
    if left < right:        # 最少有两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


a = [1, 9, 7, 6, 5, 4, 3, 2, 8]
print(a)
quick_sort(a, 0, len(a)-1)
print(a)