# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  函数缓存.py
@Description    :  
@CreateTime     :  2020/4/26 17:36
------------------------------------
@ModifyTime     :
LRU(Least Recently Used)把耗时的函数结果保存起来,避免传入相同的参数重复计算。
但缓存不会无限储存,一段时间不用,或者数量超出一定限制, 旧缓存就会扔掉。

# 参数
maxsize为最多缓存的次数，如果为None，则无限制，设置为2n时，性能最佳;
typed如果设置为True，表示不同参数类型结构分开保存，如(1和1.0)区分开
"""
from functools import lru_cache
import time


def timefun(func):
    '''
    使用装饰器实现计算每个函数消耗的时间
    :param func:
    :return:
    '''
    print()

    def innerfun(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数{func.__name__}运行时间: {end - start}")
        return result
    return innerfun


@lru_cache(maxsize=None, typed=False)
@timefun
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return sum(i for i in range(x, y))


def main():
    print('----第一次计算---')
    print(add(1, 20000000))
    print('----第二次计算---')
    print(add(1, 20000000))
    print('----计算其他---')
    print(add(2, 20000000))


if __name__ == '__main__':
    main()