# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  字符串.py
@Description    :  
@CreateTime     :  2020/4/15 18:13
------------------------------------
@ModifyTime     :  
"""


def main():
    usually_method_4()


def usually_method_4():
    str1 = '_'
    list = ['hello', 'world', 'hello', 'china']

    # 列表转字符串
    print(str1.join(list))
    print(''.join(list))

    str2 = ' '
    str3 = '12asdf'
    str4 = '234'
    str5 = 'asdf'
    # 空格
    print(str2.isspace())
    # 字母或数字
    print(str3.isalnum())
    # 数字
    print(str4.isdigit())
    # 字母
    print(str5.isalpha())


def usually_method_3():
    str = 'Hello World HELLO CHINA'
    print(str.upper())
    print(str.lower())

    str1 = 'hello'
    print(str1.ljust(10) + 'a')
    print(str1.rjust(10))
    print(str1.center(15) + 'a')

    str2 = ' hello  '
    print(str2.lstrip())
    print(str2.rstrip())
    print(str2.strip())

    # 按所给字符串对原字符串进行分割成三部分，返回元组
    print(str.partition('HELLO'))


def usually_method_2():
    str = 'hello world hello china'
    # 指定分割字符串个数
    print(str.split(' ', 1))

    print(str.capitalize())
    # 将字符串中每个单词的首字母大写
    print(str.title())

    print(str.startswith('hello'))
    print(str.endswith('china'))


def usually_method_1():
    str = 'hello world hello'
    # 找不到会返回-1
    print(str.find('or'))
    print(str.find('oo'))

    # 找不到会报错
    print(str.index('o'))
    # print(str1.index('oo'))

    print(str.count('o'))

    print(str.replace('hello', 'HELLO'))
    # 指定低替换次数
    print(str.replace('hello', 'HELLO', 1))


if __name__ == '__main__':
    main()