# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  集合.py
@Description    :  
@CreateTime     :  2020/4/16 10:50
------------------------------------
@ModifyTime     :  
"""


def main():
    usually_method_1()


def usually_method_1():
    # 创建集合的三种方式
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    # 此方式会将字符串拆分
    a = set('abracadabra')
    b = set([1, 'abracadabra', 3])
    print(basket, a, b)

    basket.add('huolong')
    print(basket)
    basket.update([1,2], [7,9])
    print(basket)

    basket.remove(1)
    basket.discard("3")  # 不存在不会发生错误
    print(basket)

    # 时间复杂度为O（1）
    print(3 in basket)


if __name__ == '__main__':
    main()