# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  04_search_empty.py
@Description    :  
@CreateTime     :  2020/7/15 18:40
------------------------------------
@ModifyTime     : 在用空字符串隔开的有序字符串中，查找给定字符串的位置。
"""


def search_empty(alist, target):
    if len(alist) == 0:
        return -1

    left, right = 0, len(alist)-1
    while left + 1 < right:
        while left + 1 < right and alist[left] == '':
            left += 1
        if alist[left] == '':
            left += 1
        if left > right:
            return -1

        mid = left + (right - left) // 2
        while alist[mid] == '':
            mid += 1

        if alist[mid] == target:
            return mid
        if alist[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if alist[left] == target:
        return left
    if alist[right] == target:
        return right
    return -1


def main():
    num_lst = ["", "", "", "", 1, '', '', '', 2, 3, '', 4]
    print(search_empty(num_lst, 3))


if __name__ == '__main__':
    main()