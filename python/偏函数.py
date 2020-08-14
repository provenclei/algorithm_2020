# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  偏函数.py
@Description    :  
@CreateTime     :  2020/4/26 11:53
------------------------------------
@ModifyTime     :  
"""
from operator import mul
from functools import partial


def add(a, b, c, d):
    return a + b + c + d


def main():
    print(mul(2,5))

    triple = partial(mul, 3)
    print(triple(7))

    tri = partial(add, 3, 2)
    l = tri(1, 1)
    print(l)


if __name__ == '__main__':
    main()