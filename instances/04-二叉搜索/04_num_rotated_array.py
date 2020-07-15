# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  04_num_rotated_array.py
@Description    :  
@CreateTime     :  2020/6/22 13:53
------------------------------------
@ModifyTime     :  在旋转数组中查找一个固定的数。
"""


def rotate_search_target(alist, target):
    if len(alist) <= 0:
        return -1

    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == target:
            return mid
        # if alist[mid] < target <= alist[right]:
        #     left = mid + 1
        # else:
        #     right = mid
        # 或者
        if alist[mid] <= target <= alist[right]:
            left = mid
        else:
            right = mid

    if alist[left] == target:
        return left
    if alist[right] == target:
        return right
    return -1


def main():
    num_list = [11, 13, 17, 2, 3, 5, 7]
    print(rotate_search_target(num_list, 3))


if __name__ == '__main__':
    main()