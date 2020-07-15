# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  04_search_range.py
@Description    :  
@CreateTime     :  2020/7/15 18:26
------------------------------------
@ModifyTime     :
找到一个给定目标值的开始和结束位置

思路：寻找第一个目标值位置，然后寻找最后一个目标值出现的位置。
"""


def search_appear_first(alist, target):
    '''
    寻找重复数组中，target第一次出现的位置
    :return:
    '''
    if len(alist) <= 0:
        return -1

    left, right = 0, len(alist)-1
    while left+1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            right = mid
        elif alist[mid] > target:
            right = mid
        else:
            left = mid
    if alist[left] == target:
        return left
    if alist[right] == target:
        return right
    return -1


def search_appear_last(alist, target):
    '''
    寻找重复数组中，target最后一次出现的位置
    :return:
    '''
    if len(alist) <= 0:
        return -1

    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            left = mid
        elif alist[mid] > target:
            right = mid
        else:
            left = mid
    if alist[left] == target:
        return left
    if alist[right] == target:
        return right
    return -1


def search_range(alist, target):
    if len(alist) <= 0:
        return (-1, -1)
    lbound, rbound = -1, -1
    # search for left bound
    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            right = mid
        elif (alist[mid] < target):
            left = mid
        else:
            right = mid

    if alist[left] == target:
        lbound = left
    elif alist[right] == target:
        lbound = right
    else:
        return (-1, -1)

    # search for right bound
    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            left = mid
        elif (alist[mid] < target):
            left = mid
        else:
            right = mid

    if alist[right] == target:
        rbound = right
    elif alist[left] == target:
        rbound = left
    else:
        return (-1, -1)

    return (lbound, rbound)


def main():
    num_lst = [1, 3, 3, 3, 6, 6, 6, 6, 6, 6, 7, 9]
    print(search_appear_first(num_lst, 6))
    print(search_appear_last(num_lst, 9))
    print(search_range(num_lst, 6))


if __name__ == '__main__':
    main()