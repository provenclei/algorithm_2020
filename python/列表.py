# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  列表.py
@Description    :  
@CreateTime     :  2020/4/16 10:24
------------------------------------
@ModifyTime     :  
"""


def main():
    list_1 = ['a', 'b', 'a', 'd']
    list_1.append('f')
    print(list_1)

    print(list_1.count('a'))
    list_1.reverse() # 无返回值
    print(list_1)
    list_1.pop()
    print(list_1)

    list_2 = [2,35,65]
    # 追加多个元素
    list_1.extend(list_2) # 在原列表中进行操作，无返回值
    print(list_1)

    print(list_1.index('a', 1))
    list_2.sort(reverse=True)
    print(list_2)

    list_3 = [('a', 8), ('c', 3), ('d', 10), ('e', 5)]
    list_3.sort(key=lambda lst: lst[1])
    print(list_3)


if __name__ == '__main__':
    main()