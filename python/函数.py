# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  函数.py
@Description    :  
@CreateTime     :  2020/4/17 16:57
------------------------------------
@ModifyTime     :  
"""
from functools import reduce


def main():
    # printinfo('tl')
    # var_fuc(1,'a','b',name='zhang',age=20)

    # 可变对象和不可变对象之间的参数传递
    # strings, tuples, 和 numbers 是不可更改的对象，而 list,dict,set等则是可以修改的对象。
    # 调用changeme函数
    # mylist = [10, 20, 30]
    # changeme(mylist)
    # print("函数外取值: ", mylist)

    # 迭代器
    # 优势：分批加载进内存，节省内存空间。
    # list = [1, 2, 3, 4, 5, 6, 7]
    # it = iter(list)  # 创建迭代器对象
    # print(next(it))  # 输出迭代器的下一个元素 1 print (next(it))

    # 生成器
    # 使用了 yield 的函数被称为生成器。
    # 生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
    # a = f()
    # print(next(a))
    # print(next(a))
    # print(next(a))

    # 斐波那契数列
    # fibb = fib(6)
    # print([next(fibb) for i in range(6)])

    # 变量作用域
    # 对于不可变类型的全局变量来说，要在函数中修改需要global声明
    # total = 0  # 定义了一个全局变量
    # print(sum(10, 20))
    # print("函数外：%d" % total)

    # 高阶函数
    # lst = [('a', 3), ('c', 7), ('f', 4), ('s', 2)]
    # print(sorted(lst, key=lambda item: item[1], reverse=True))

    # num = 1
    # print(isinstance(num, int))

    # print(eval('1+1'))

    # map 映射
    # list01 = [1, 3, 5, 7, 9]
    # list02 = [2, 4, 6, 8, 10]
    # new_list = map(lambda x, y: x * y, list01, list02)  # ↓将map转化为list 计算
    # print(list(new_list))

    # filter 过滤掉不符合条件的元素 筛选
    # list02 = [2, 0, 4, 6, 8, 10]
    # # 传入函数返回值为True or False
    # # 以下匿名函数的作用是获取非0元素
    # new_list = filter(lambda x: x, list02)
    # # new_list = filter(lambda x: x > 4, list02)
    # print(list(new_list))

    # reduce 简单理解，就是把列表，元组的成员按照既定的规则累加 相当于求总和
    list02 = [2, 4, 6, 8, 10]
    # ↓初始值为0在末尾，省略后结果一致，如果给到1，结果+1
    new_list = reduce(lambda x, y: x + y, list02, 0)
    print(new_list)


def sum(a,b):
    # 当内部作用域想要修改外部作用域的变量的时候，就可以用到global关键字了。
    global total
    total = a+b
    print("函数内：%d" % total)
    return total


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


def f():
    print('start')
    a = yield 1
    print(a)
    print('middle....')
    b = yield 2  # 2这个值只是迭代值，调用next时候返回的值 print(b)
    print('next')
    c = yield 3
    # 最后一个yield之后的数字不会被打印出来
    print(c)


def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 函数参数：
# 默认参数
# 不定长参数
def printinfo( name, age = 35 ):
    "打印任何传入的字符串"
    print ("Name: ", name)
    print ("Age ", age)
    return


def var_fuc(a, *tuple_arg, **dict_arg):
    print(a)
    print(tuple_arg)
    print(dict_arg)


if __name__ == '__main__':
    main()