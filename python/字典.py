# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  字典.py
@Description    :  
@CreateTime     :  2020/4/16 10:50
------------------------------------
@ModifyTime     :  
"""


def main():
    # usually_method_1()
    # usually_method_2()
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    lst = list(enumerate(seasons, start=1))  # 下标从 1 开始 [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
    print(lst)

    names = ['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe', 'Alice', 'Sherry', 'Eva']
    print(list(enumerate(names)))
    name = {k: v for k, v in enumerate(names)}
    print(name)


def usually_method_2():
    students = {
        'Jhon': {'age': 12, 'number': 322235},
        'Peter': {'age': 17, 'number': 546344},
        'Tom': {'age': 6, 'number': 434657}
    }
    for key, value in students.items():
        # age, number = value['age'], value['number']
        age, number = students[key].values()
        print('number:%d, name:%s, age:%d' % (number, key, age))

    for key in students.keys():
        print(key)


def usually_method_1():
    dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
    # 取值的三种方法
    # 1. get, 没找到返回None
    print(dict.get('sadf'))
    # 2. dict[''], 键值不存在直接报错
    # print(dict['sadf'])
    # 3. setdefault:不存在返回None，并插入新的键值为None, 存在返回值。
    print(dict.setdefault('Beth'))
    print(dict.setdefault('AER'))
    print(dict)

    # 将多个键值对更新到字典中
    dict_2 = {'aa': 1243, 'ere': 3333}
    dict.update(dict_2)
    print(dict)


if __name__ == '__main__':
    main()