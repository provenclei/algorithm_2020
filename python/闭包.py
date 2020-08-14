# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  闭包.py
@Description    :  
@CreateTime     :  2020/4/26 16:14
------------------------------------
@ModifyTime     :
一个函数定义中引入函数外定义的变量，并且该函数在定义环境外执行，这种函数称为闭包。
装饰器本质上就是闭包。
"""
import time


def outer_func():
    loc_list=[]
    name='zhangsan'
    age=10
    m=[1,2]

    def inner_func(name):
        m.append(len(loc_list))
        s=sum(m)
        loc_list.append(len(loc_list)+1)
        print(f"{name} loc_list={loc_list} ,sum of m {s},age is {age}")
    # 返回必须是内部函数名
    return inner_func


def main():
    o=outer_func()
    # 调用一次外部函数，创建一次函数内部空间
    close = outer_func()
    close("f0")  # 1
    close("f0")  # 2
    close1 = outer_func()
    close("f0")  # 3
    close("f0")  # 4
    close1("f1")  # 1
    close1("f1")  # 2

    print(sum_all(1000000))

    fs1, fs2, fs3 = my_func_1()
    print(fs1(), fs2(), fs3())

    f1, f2, f3 = my_func_2()
    print(f1(), f2(), f3())


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


@timefun
def sum_all(size):
    return sum(i for i in range(size))


def my_func_1(*args):
    '''
    闭包的陷阱1
    :param args:
    :return:
    '''
    fs = []
    for i in range(3):
        # i的最终状态是2，所以返回值始终为4
        def func():
            return i * i
        fs.append(func)
    return fs


def my_func_2(*args):
    '''
    闭包的陷阱2
    :param args:
    :return:
    '''
    fs = []
    for i in range(3):
        # 将i当做参数传入函数
        def func(_i=i):
            return _i * _i
        fs.append(func)
    return fs


if __name__ == '__main__':
    main()