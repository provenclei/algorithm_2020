# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  多继承.py
@Description    :  
@CreateTime     :  2020/4/24 10:18
------------------------------------
@ModifyTime     :  
"""


class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        super().__init__()
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))

    def calc(self):
        return int(self.grade) / int(self.age)


# 另一个类，多重继承之前的准备
class Speaker(object):
    topic = ''
    name = ''

    def __init__(self, n, t):
        # 一个Python类，即使直接派生自object，最好也调用一下super().__init__，
        # 不然可能造成多重继承时派生层次中某些类的__init__ 被跳过。
        # super().__init__()
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = 'sample_class'
    __private = 'cannot'

    def __init__(self, n, a, w, g, t):
        Speaker.__init__(self, n, t)
        Student.__init__(self, n + "_other", a, w, g)  # 多个父类初始化时具有相同属性时，以最后一次赋值为准

    def print(self):
        print(Sample.__private)


class A(object):
    def __init__(self):
        print('A enter')
        super(A, self).__init__()
        print('A leave')


class B(object):
    def __init__(self):
        print('B enter')
        super(B, self).__init__()
        print('B leave')


class C(object):
    def __init__(self):
        print('C enter')
        super(C, self).__init__()
        print('C leave')


class D(A, B, C):
    def __init__(self):
        print('D enter')
        super(D, self).__init__()
        print('D leave')


def main():
    test = Sample("Tim", 25, 80, 4, "Python")
    test.speak()  # 方法名同，默认调用的是在括号中排前(靠左)地父类的方法
    test.print()
    # c_name=test.__private+"name"
    print(test.calc())
    # print(test.__private)

    d = D()
    print()


if __name__ == '__main__':
    main()