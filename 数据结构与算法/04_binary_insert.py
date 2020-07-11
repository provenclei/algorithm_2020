# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  04_binary_insert.py
@Description    :  
@CreateTime     :  2020/6/22 11:27
------------------------------------
@ModifyTime     :
                    如果存在，返回索引
                    如果不存在，返回插入位置
"""


def binary_search(alist, item):
    if len(alist) <= 0:
        return -1
    left, right = 0, len(alist)-1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if item > alist[mid]:
            left = mid
        elif item < alist[mid]:
            right = mid
        elif item == alist[mid]:
            right = mid
    if alist[left] == item:
        return left
    if alist[right] == item:
        return right
    return f'插入在{left}和{right}之间'


def main():
    num_list = [1, 2, 3, 4, 5, 7, 9]
    print(binary_search(num_list, 4))
    print(binary_search(num_list, 6))


if __name__ == '__main__':
    main()