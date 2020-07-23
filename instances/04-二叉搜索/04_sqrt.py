# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  04_sqrt.py
@Description    :  
@CreateTime     :  2020/7/24 00:26
------------------------------------
@ModifyTime     :  
"""


def sqrt(x):
    if x == 0:
        return 0
    left, right = 1, x
    while left < right:
        mid = left + (right - left) // 2
        if mid == x // mid:
            return mid
        if mid < x // mid:
            left = mid + 1
        else:
            right = mid - 1
    return right


def main():
    print(sqrt(40))


if __name__ == '__main__':
    main()