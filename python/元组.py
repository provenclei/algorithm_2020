# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  元组.py
@Description    :  
@CreateTime     :  2020/4/16 09:30
------------------------------------
@ModifyTime     :  
"""


def main():
    usually_method_2()


def usually_method_2():
    # 列表转元组
    lst = ['a', 's', 'a', 'r']
    tuple_lst = tuple(lst)
    print(tuple_lst)

    tuple_1 = (3, 6, 2, 5, 1)
    print(len(tuple_1), max(tuple_1), min(tuple_1))


def usually_method_1():
    tuple_1 = (234, 'asdf', '你好')
    print(tuple_1)
    # int类型
    tuple_2 = (1)
    print(type(tuple_2), tuple_2)
    # tuple
    tuple_3 = (1,)
    print(type(tuple_3), tuple_3)


if __name__ == '__main__':
    main()