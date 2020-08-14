# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  类方法和静态方法.py
@Description    :  
@CreateTime     :  2020/4/24 10:54
------------------------------------
@ModifyTime     :
@classmethod @staticmethod区别:
@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
@classmethod 是一个函数修饰符，它表示接下来的是一个类方法，而对于平常我们见到的则叫做实例方法。
类方法的第一个参数cls，而实例方法的第一个参数是self，表示该类的一个实例。
普通对象方法至少需要一个self参数，代表类对象实例。
类方法有类变量cls传入，从而可以用cls做一些相关的处理。并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。
"""

d = {'kernel': [[1, 2, 1], [1, 2, 3], [3, 3, 3]], 'dropout': 1.0, 'deep': 10, 'activate': 'relu'}
d1 = {'kernel': [[1, 1, 1], [1, 1, 1], [1, 3, 3]], 'dropout': 0.0, 'deep': 1, 'activate': 'relu'}


class A(object):
    model_name = '图像识别'
    instance = None
    __slot__ = ['foo', 'model_name', 'instance']

    def __new__(cls, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)  # super().__new__(cls)
            for k, v in kwargs.items():
                setattr(cls, k, v)
        return cls.instance

    # 实例方法
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)

    # 类方法
    # 不能访问实例属性
    # 参数必须传入cls
    # 必须传入cls参数(即代表了此类对象 - ----区别 - -----self代表实例对象)，并且用此
    # 来调用类属性: cls.类属性名
    @classmethod
    def class_foo(cls, x):
        if not isinstance(x, dict):
            raise ValueError("input invalid !!!")
        for k, v in x.items():
            setattr(cls, k, v)
            # cls.k=v
        print("load model success")

    # 静态方法：
    # 通过装饰器 @staticmethod 装饰
    # 不能访问实例属性
    # 参数不能传入self
    # 与类相关但是不依赖类与实例的方法
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)

    @classmethod
    def get_instance(cls):
        if A.instance is None:
            A.instance = object.__new__(A)
        return A.instance


def main():
    A.static_foo('static')
    B = A.class_foo(d)
    a1 = A.get_instance()
    a2 = A.get_instance()
    a3 = A()
    a1.model_name = 'nlp'
    print(a3.model_name)
    a3.class_foo(d1)
    print(a3.foo('self'))


if __name__ == '__main__':
    main()