# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  装饰器.py
@Description    :  
@CreateTime     :  2020/4/26 12:13
------------------------------------
@ModifyTime     :  
"""
r=[]


def reg(func):
    print(f"running register {func} ")

    r.append(func)
    return func


@reg
def f1():
    print("running f1()")


@reg
def f2():
    print("running f2()")


@reg
def f3():
    print("running f3()")


def main():
    print("running main()")
    print("registry ->", reg)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()