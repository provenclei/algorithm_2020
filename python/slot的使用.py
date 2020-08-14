# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  slot的使用.py
@Description    :  
@CreateTime     :  2020/4/26 09:54
------------------------------------
@ModifyTime     :  
"""
from types import MethodType
# 用MethodType将方法绑定到实例, 每个实例有自己单独的指向区域，互不干扰.
# 用MethodType将方法绑定到类, 其子类的实例也能使用此方法.
# 使用MethodType会创建一个link指向外部的方法, 在创建实例或子类的实例时此link也会被复制.


class Student(object):
    # 如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。
    __slots__ = ('name', 'age', 'score')

    def set_age(self, age):
        self.age = age

    def set_score(self, score):
        self.score = score


class GraduateStudent(Student):
    pass


def main():
    # 当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法
    s1 = Student()
    s1.name = 'Michael'
    print(s1.name)

    # 给该实例绑定属性的另一种方法
    # s1.set_age = MethodType(set_age, s1)  # 给实例绑定一个方法
    # s1.set_age(23)
    # print(s1.age)

    # 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
    s2 = Student()
    # s2.set_age(24)

    # 为了给所有实例都绑定方法，可以给class绑定方法：
    # 以下方法相当于添加了一个类属性
    # Student.set_score = MethodType(set_score, Student)
    s1.set_score(60)
    print(s1.score)
    s2.set_score(100)
    print(s2.score)
    print(s1.score)

    # __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
    g = GraduateStudent()
    g.sex = 'man'
    print(g.sex)


if __name__ == '__main__':
    main()