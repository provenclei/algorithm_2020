# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  作业(3.1).py
@Description    :  
@CreateTime     :  2020/4/24 17:07
------------------------------------
@ModifyTime     :
练习1：
1、编写一个学生类，提供 name、age、gender、phone、address、email等属性，为学生类提供带所有成员变量的构造器，为学生类提供方法，用于描绘吃、喝、玩、睡等行为。
2、 利用前面定义的 Student 类，定义一个列表保存多个 Student 对象作为通讯录数据。程序可通过 name、email、address 查询，如果找不到数据，则进行友好提示。

练习2:王者荣耀小游戏
1、创建三个游戏人物，分别是:
属性:  名字:name,定位:category,血量:Output技能:Skill
英雄:
    铠，战士，血量:1000 技能:极刃风暴
    王昭君，法师 ，血量:1000 技能:凛冬将至
    阿轲，刺客，血量:1000 技能:瞬华
2、游戏场景，分别:
    偷红buff，释放技能偷到红buff消耗血量300
    solo战斗，一血，消耗血量500
    补血，加血200
"""


class Student(object):
    def __init__(self, name, age, gender, phone, address, email):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email

    def __new__(cls, *args, **kwargs):
        label = ['name', 'age', 'gender', 'phone', 'address', 'email']
        if not hasattr(cls, 'data_lst'):
            setattr(cls, 'data_lst', [])
        dict = {k: v for k, v in zip(label, args)}
        org_lst = getattr(cls, 'data_lst')
        org_lst.append(dict)
        setattr(cls, 'data_lst', org_lst)
        object.__new__(cls)
        return super(Student, cls).__new__(cls)

    def eat(self):
        print(f'{self.name} 正在吃东西。。。')

    def drink(self):
        print(f'{self.name} 正在喝东西。。。')

    def play(self):
        print(f'{self.name} 正在玩。。。')

    def sleep(self):
        print(f'{self.name} 正在睡觉。。。')


class Hero(object):
    def __init__(self, name, category, output, skill):
        self.name = name
        self.category = category
        self.output = output
        self.skill = skill

    def buff(self):
        self.output -= 200
        print(f'{self.category}{self.name}释放{self.skill}技能偷到红buff消耗血量300,剩余血量：{self.output}')

    def solo(self):
        self.output -= 500
        print(f'{self.category}{self.name}释放{self.skill}solo战斗，一血，消耗血量500,剩余血量：{self.output}')

    def add_blud(self):
        self.output += 200
        print(f'{self.category}{self.name}释放{self.skill}补血，加血200,剩余血量：{self.output}')


def main():
    practice_1()
    practice_2()


def practice_2():
    kai = Hero('铠', '战士', 1000, '极刃风暴')
    zhaojun = Hero('王昭君', '法师', 1000, '凛冬将至')
    ake = Hero('阿轲', '刺客', 1000, '瞬华')

    kai.solo()
    zhaojun.add_blud()
    ake.buff()


def practice_1():
    s_1 = Student('SHE', 20, 'female', '13920203843', '深圳', '1234@163.com')
    s_1.eat()

    s_2 = Student('Beyond', 44, 'man', '13877298332', '香港', '5563@163.com')
    data_lst = Student.__dict__['data_lst']
    # 并不是多有dict中的值都能获得的
    print(data_lst)

    key = input('请输入键：')
    value = input('请输入值：')
    for item in data_lst:
        if not item.get(key):
            print('您找的键不存在')
        elif item.get(key) != value:
            print('您找的键不存在')
        else:
            print(f'您找的信息：{item}')
            break
    print()


if __name__ == '__main__':
    main()