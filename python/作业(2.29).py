# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  作业(2.29).py
@Description    :  
@CreateTime     :  2020/4/17 16:57
------------------------------------
@ModifyTime     :  
"""
from functools import reduce


def main():
    '''
    作业1、用递归方式生成斐波拉契数列（用一个递归函数实现）
    作业2、用递归方式求n!
    作业3、格式化用户的英文名，要求首字母大小，其它字母小写
    作业4、将用户英文名、年龄、性别三个集合的数据结合到一起，形成一个集合
    作业5、过滤性别为男的用户
    作业6、求性别为男的用户的平均年龄
    :return:
    '''
    # 作业1、用递归方式生成斐波拉契数列（用一个递归函数实现）
    # print([fibb(i) for i in range(6)])

    # 作业2、用递归方式求n!
    # print(jie(5))

    # 作业3、格式化用户的英文名，要求首字母大小，其它字母小写
    # names = ['jOoei', 'ifIFJ', 'SIXdff', 'lOSDni']
    # names_filter = map(lambda item: item.lower().title(), names)
    # print(list(names_filter))

    # 作业4、将用户英文名、年龄、性别三个集合的数据结合到一起，形成一个集合
    name = ['a', 'b', 'c']
    age = [12, 15, 17]
    sex = ['man', 'fenal', 'man']
    info = list(map(lambda name, age, sex: (name, age, sex), name, age, sex))
    print(info)

    # 作业5、过滤性别为男的用户
    info_filter = list(filter(lambda item: item[2] == 'man', info))
    print(info_filter)

    # 作业6、求性别为男的用户的平均年龄
    age_sum = reduce(lambda x, y: x[1] + y[1], info_filter)
    print(age_sum/len(info_filter))


def jie(n):
    if n <= 1:
        return 1
    return n * jie(n-1)


def fibb(n):
    if n <= 1:
        return 1
    return fibb(n-1) + fibb(n-2)


if __name__ == '__main__':
    main()