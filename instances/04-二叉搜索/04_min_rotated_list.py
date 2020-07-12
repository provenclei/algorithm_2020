# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  04_min_rotated_list.py
@Description    :  
@CreateTime     :  2020/6/22 12:05
------------------------------------
@ModifyTime     :  在按某个轴翻转过后的有序数组中，寻找最小值
"""


def rotate_search(alist):
    if len(alist) <= 0:
        return -1
    left, right = 0, len(alist) - 1
    while left + 1 < right:
        # 当 left < right 时，数列有序
        if alist[left] < alist[right]:
            return alist[left]
        midd = left + (right - left) // 2
        if alist[midd] > alist[left]:
            left = midd + 1
        else:
            right = midd
    return alist[left] if alist[left] < alist[right] else alist[right]


def main():
    num_list = [11, 13, 17, 2, 3, 5, 7]
    print(rotate_search(num_list))
    num_list = [2, 3, 5, 7, 11, 13, 17]
    print(rotate_search(num_list))


if __name__ == '__main__':
    main()