# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  继承和反射.py
@Description    :  
@CreateTime     :  2020/4/20 16:12
------------------------------------
@ModifyTime     :  
"""


class People(object):
    # 类变量:类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。
    # 类变量通常不作为实例变量使用。如果需要用在函数中使用类名.类属性。
    name = ""
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0  # private：只能本类调用
    _addr = 'shanghai'  # protect:只能本类或者子类调用

    # 定义构造方法
    def __init__(self, name, age, weight):
        super().__init__()
        # 实例变量: 定义在方法中的变量，只作用于当前实例的类。
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print("i am a peaple, %s 说: 我 %d 岁。" % (self.name, self.age))

    def cal_score(self):
        ratio = self.age / self.__weight
        return ratio

    # 每创建一个实例，系统会自动创建一个对应的字典，可以更新字典中的内容
    def add_item(self, d, **dict_arg):
        d.update(dict_arg)


# 单继承
class Student(People):
    grade = ''

    def __init__(self, name, age, weight, grade):
        # 调用父类的构造函数
        # People.__init__(self, name, age, weight)
        # super(Student,self).__init__(name, age, weight)
        super().__init__(name, age, weight)
        self.grade = grade

    # 覆写父类的方法
    def speak(self):
        print("i am a student, %s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


class Teacher(People):

    def speak(self):
        print('i am a teacher')


# 多继承
class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")


class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("leave A")


class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")


class C(A, B):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")


def main():
    # 单继承
    s = Student('ken', 10, 60, 3)
    # print(s.__weight)  # 不能访问私有属性
    print(s._addr)
    s.speak()

    # 多继承
    # Python 中有一个列表叫 MRO，它的全称是 Method Resolution Order，即方法解析顺序列表。
    # 对于我们定义的每个类，它都会根据一种特定的算法(C3线性算法，这里不作深入讨论)来得到一个列表，这个列表代表了类继承的顺序。
    # 我们可以通过 c.__class__.mro() 方法来查看某个类的 MRO 列表：
    # [__main__.C, __main__.A, __main__.B, __main__.Base, object]
    # super() 执行的过程可以总结为两步：
    # 根据我们传入的实例对象，通过 instance.__class__.mro() 得到当前类的 MRO 列表
    # 根据列表的顺序，取列表的第二个元素，返回

    # 它有三个原则：
    # 1.子类一定在父类前面
    # 2.如果存在多个父类，它会根据 MRO 列表顺序来执行
    # 3.如果多个父类存在相同方法，会根据 MRO 列表选择第一个符合的类
    c = C()

    print()

    # 多态
    p = People('tl', 22, 111)
    stu = Student('bb', 21, 222, 1)
    t = Teacher('zb', 23, 132)
    p.speak()
    stu.speak()
    t.speak()


def fun(obj):
    '''
    多态
    :param obj: 传入对象
    :return:
    '''
    obj.speak()


def example_1():
    # 实例化类
    p = People('runoob', 10, 30)
    p.add_item(p.__dict__, method='eat', tel=13918948888)
    p.speak()

    # 访问实例属性
    age_instance = p.age
    print(age_instance)

    # 访问类属性
    age_class = People.age
    print(age_class)

    # 反射
    age_p = getattr(p, 'age')  # 访问对象的属性
    print(age_p)
    has_attr = hasattr(p, 'age')  # 检查是否存在一个属性
    print(has_attr)

    # 等价于：p.tel = 13013459888
    setattr(p, 'tel', 13013459888)  # 设置一个属性。如果属性不存在，会创建一个新属性
    setattr(p, 'age', 30)  # 设置一个属性。如果属性不存在，会创建一个新属性
    print(p.tel)
    print(p.age)
    # 通过反射机制设置的属性，无法通过has_attr方法得到
    # print(has_attr(p, 'tel'))
    print(getattr(p, 'tel'))

    delattr(p, 'age')
    # 删除了实例属性，直接访问类属性
    print(p.age)
    # 删除一个不存在的属性会直接报错
    # delattr(p, 'score')

    # 使用反射机制设置类属性
    setattr(People, 'height', '173')
    print(People.height)


class Abc():
    c = 0
    b = ''
    __x = 'private'
    _v = 'protect'

    def fun(self):
        print('Abc')


def example_2():
    a = Abc()
    a.__setattr__('d', 4)
    print(a.d, a.c)

    # 通过反射可以生成 public,protect,private 级别的属性，并通过反射获取
    setattr(a, 'e', 5)
    setattr(a, '_f', 6)
    setattr(a, '__g', 7)
    print(a.e, getattr(a, '_f'), a.__getattribute__('__g'))

    # 反射可以获取列中本来就有的 public,protect 级别的属性，无法获取 private 的属性
    print(getattr(a, '_v'))
    print()


if __name__ == '__main__':
    main()