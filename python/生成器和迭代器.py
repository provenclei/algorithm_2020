# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  生成器和迭代器.py
@Description    :  
@CreateTime     :  2020/4/26 17:48
------------------------------------
@ModifyTime     :
生成器(generator)
    生成器是一个对象，而且是可迭代的，它保存的是算法，只有在用的时候调用它它才会去计算，这样就节省了大量的空间。
生成器有两种创建方式：
方法一：
    创建生成器方法1:把列表生成式的 [ ] 改成 ( )
    generator1 =(x*2 for x in range(10))
方法二:
    使用yield函数创建生成器

迭代器：
    迭代器是一个可以记住遍历的位置的对象。
    迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
    迭代器只能往前不会后退。
    除了字符串、列表、元组、字典和文件等数据结构是迭代对象，只要对象实现了iter()和next()两个方法，就可以被迭代访问。
    iter()用来生成迭代器，next()用来返回迭代器的下一个数 据。
"""


class MyIter(object):
    def __init__(self, total, start=0):
        self.total = total
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.total:
            self.start += 1
            return self.start
        else:
            raise StopIteration


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a,  b = b, a + b
        n += 1
    return 'done'


def main():
    # 迭代器
    myiter = MyIter(5)
    it = iter(myiter)
    for i in it:
        print(i)

    # 生成器
    generator = (x * 2 for x in range(10))
    print(generator)

    # 生成器实现斐波那契数列
    for i in fib(6):
        print(i)


if __name__ == '__main__':
    main()