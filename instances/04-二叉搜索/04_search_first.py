# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  04_search_first.py
@Description    :  
@CreateTime     :  2020/7/15 19:22
------------------------------------
@ModifyTime     :
                    在有序的数据流中，查找某一个元素第一个出现的位置。（倍增法）

                    此题在数据流中寻找1的位置。

                    数据流的特点：长度未知
"""

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


def search_first(alist):
    left, right = 0, 1
    while alist[right] == 0:
        left = right
        right *= 2

        if right > len(alist):
            # 越界
            right = len(alist) - 1
            break
    return left + search_range(alist[left:right+1], 1)[0]


def main():
    alist = [0, 0, 0, 0, 0, 1]
    print(search_first(alist))


if __name__ == '__main__':
    main()