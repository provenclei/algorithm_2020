# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  search_insert_position.py
@Description    :  
@CreateTime     :  2020/6/22 14:31
------------------------------------
@ModifyTime     :
搜索插入位置

给定有序数组和一个目标值，如果在数组中找到此目标值则返回目标值的index，如果 没有找到，则返回目标值按顺序应该被插入的位置index.

注:可以假设数组中不存在重复数。
"""


def search_insert_position(alist, target):
    if len(alist) <= 0:
        return -1

    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            return mid
        if alist[mid] < target:
            left = mid
        else:
            right = mid
    if alist[left] >= target:
        return left
    if alist[right] >= target:
        return right
    return right + 1


def main():
    num_list = [2, 3, 5, 7, 11, 13, 17]
    print(search_insert_position(num_list, 8))


if __name__ == '__main__':
    main()