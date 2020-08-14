# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  单例.py
@Description    :  
@CreateTime     :  2020/4/24 10:04
------------------------------------
@ModifyTime     :  
"""
d={'kernel':[[1,2,1],[1,2,3],[3,3,3]],'dropout':1.0,'deep':10,'activate':'relu'}


class Singleton(object):
    # _instance = None
    #
    # def __new__(cls, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = object.__new__(cls)  # super().__new__(cls)
    #         for k,v in kwargs.items():
    #             setattr(cls, k, v)
    #     return cls._instance

    # 优化
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            for k, v in kwargs.items():
                setattr(cls, k, v)
            for item in args:
                setattr(cls, item)
            setattr(cls, '_instance', object.__new__(cls))
        return getattr(cls, '_instance')

    # def __new__(cls):
    #     # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Singleton, cls).__new__(cls)
    #     return cls.instance


def main():
    # 示例：
    # 使用a.__class__.__dict__可以查看Singleton中dict字典的元素
    a = Singleton(kernel=[[1, 2, 1], [1, 2, 3], [3, 3, 3]], dropout=1.0, deep=10, activate='relu')
    b = Singleton()
    c = Singleton()
    print(id(a), id(b), id(c))


if __name__ == '__main__':
    main()