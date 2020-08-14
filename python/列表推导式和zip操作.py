# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  列表推导式和zip操作.py
@Description    :  
@CreateTime     :  2020/4/25 22:30
------------------------------------
@ModifyTime     :  
"""
from itertools import zip_longest
from itertools import chain
import time
from itertools import product


def main():
    zip_p()


def zip_p():
    '''
    zip操作
    :return:
    '''
    x = [[1], 2, 3, 4, 5]
    y = ['a', 'b', 'c', 'd', 'e']
    z = ['a1', 'b2', 'c3', 'd4', 'e5']
    # 返回值为一个对象
    print(zip(x, y, z))
    for i in zip(x, y, z):
        print(i)

    print('*'*20)

    # 不等长序列遍历
    x = [1, 2, 3, 4, 5, 6]
    y = ['a', 'b', 'c', 'd', 'e']
    for i in zip_longest(x, y):
        print(i)

    print('*' * 20)

    # 拉平嵌套
    li = [[1, 2], [3, 4], [5, 6]] * 1000000
    t = time.time()
    l1 = list(chain.from_iterable(li))
    print(f"---cost1 {time.time() - t}")

    t = time.time()
    l2 = list(chain(*li))
    print(f"---cost2 {time.time() - t}")

    t1 = time.time()
    t = []
    [t.extend(i) for i in li]
    print(f"---cost3 {time.time() - t1}")

    print('*' * 20)

    # 笛卡尔积
    for x in ['a', 'b', 'c']:
        for y in ['d', 'e', 'f']:
            for z in ['m', 'n']:
                print(x, y, z)
    print('另一种方式：')
    for x, y, z in product(['a', 'b', 'c'], ['d', 'e', 'f'], ['m', 'n']):
        print(x, y, z)


def lst_p():
    '''
    列表推导式
    :return:
    '''
    num = [1, 2, 3]
    # 链式推导使用（）会产生一个生成器
    myvec=([x, x*2] for x in num)
    print(myvec)
    for item in myvec:
        print(item)

    mylst = [[x, x * 2] for x in num]
    print(mylst)


if __name__ == '__main__':
    main()