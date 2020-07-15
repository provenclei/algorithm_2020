# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  04_binary_search_template.py
@Description    :  
@CreateTime     :  2020/7/15 16:21
------------------------------------
@ModifyTime     :  二分法模板
"""


def binary_search(alist, target):
    if len(alist) <= 0:
        return -1
    left, right = 0, len(alist)-1
    while left + 1 < right:
        middle = left + (right - left) // 2
        if alist[middle] == target:
            right = middle
        elif alist[middle] < target:
            left = middle
        elif alist[middle] > target:
            right = middle
    if alist[left] == target:
        return left
    if alist[right] == target:
        return right
    return '应该插在{}之后,{}之前'.format(alist[left], alist[right])


def main():
    num_list = [1, 2, 3, 3, 7, 8, 9]
    print(binary_search(num_list, 7))
    print(binary_search(num_list, 4))


if __name__ == '__main__':
    main()