# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  作业.py
@Description    :  
@CreateTime     :  2020/4/15 18:19
------------------------------------
@ModifyTime     :  
"""
import random


def main():
    # Python基础作业：
    # base_homework()

    # 字符串作业
    # str_homework()

    # 字典作业
    # dict_homework()

    # 元组
    # tuple_homework()

    # 集合
    # set_homework()

    # 课后作业
    # practice()

    # 列表推导式
    # reason_homework()

    # 循环控制语句
    # control_homework_1()
    control_homework_2()


def control_homework_2():
    '''
    1、使用for循环如何实现1-100的和(99乘法表)
    2、求m,n中矩阵对应元素的和，元素的乘积
    m = [[1,2,3], [4,5,6], [7,8,9]]
    n = [[2,2,2], [3,3,3], [4,4,4]]
    3.求一个3*3矩阵对角线元素之和
    4.names = ['Tom','Billy','Jefferson','Andrew','Wesley','Steven', 'Joe','Alice','Jill',
    'Ana','Wendy','Jennifer','Sherry','Eva']
    找出上述名字长度大于4的名字，组成列表打印出来。 过滤掉长度大于5的字符串列表，并将剩下的转换成大写字母。
    :return:
    '''

    # 1. 使用for循环如何实现1-100的和(99乘法表)
    # contr_homework_1()

    # 2. 求m,n中矩阵对应元素的和，元素的乘积
    # contr_homework_2()

    # 3.求一个3*3矩阵对角线元素之和
    # contr_homework_3()

    # 4.names = ['Tom','Billy','Jefferson','Andrew','Wesley','Steven', 'Joe','Alice','Jill',
    #     'Ana','Wendy','Jennifer','Sherry','Eva']
    #     找出上述名字长度大于4的名字，组成列表打印出来。 过滤掉长度大于5的字符串列表，并将剩下的转换成大写字母。
    contr_homework_4()


def contr_homework_1():
    '''
    使用for循环如何实现1-100的和(99乘法表)
    :return:
    '''
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f'{i}*{j}={i*j} ', end="")
        print()


def contr_homework_2():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    n = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
    lst = []
    for i in range(3):
        item = []
        for j in range(3):
            tmp = m[i][j] + n[i][j]
            item.append(tmp)
        lst.append(item)
    print(lst)


def contr_homework_3():
    m = [
        [1, 2, 3],
        [3, 4, 5],
        [4, 6, 7]
    ]
    sum = 0
    for i in range(3):
        for j in range(3):
            sum += m[i][j] if i == j else 0
    print(sum)


def contr_homework_4():
    names = ['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe', 'Alice', 'Jill',
             'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']
    print([name for name in names if len(name) > 4])
    print([name.upper() for name in names if len(name) >= 5])


def reason_homework():
    '''
    1.names = ['Joe','Bill','Jefferson','Andy','Wesley','Keven','Tom', 'Alice','Jill','Ana','Wendy','Jenny','Sherry','Eva']
    找出上述名字中长度大于4的名字,组成列表打印出来. 过滤掉长度小于5的字符串列表，并将剩下的转换成大写字母.
    2、快速创建一个包含1-10之间所有偶数的列表
    :return:
    '''
    names = ['Joe', 'Bill', 'Jefferson', 'Andy', 'Wesley', 'Keven', 'Tom', 'Alice', 'Jill', 'Ana', 'Wendy', 'Jenny',
             'Sherry', 'Eva']
    print([name for name in names if len(name) > 4])
    print([name.upper() for name in names if len(name) >= 5])
    print([i for i in list(range(1, 11)) if i % 2 == 0])


def control_homework_1():
    # 题目:随机输入一些成绩，利用条件运算符的嵌套学习成绩>=90分的同学用A表示，60-89分之 间的用B表示，60分以下的用C表示。
    # con_homework_1()

    # 题目:Python 剪刀石头布小游戏程序
    # 1.你输入‘剪刀’，‘石头’，‘布’，其中一个。
    # 2.电脑随机生成‘剪刀’，‘石头’，‘布’。
    # 3.两者结果进行对比，并进行判断胜负，并输出结果
    # a) 你赢了
    # b) 你输了
    # c) 打和了，重新循环，直至决出结果
    # con_homework_2()

    # *
    # **
    # ***
    # ****
    # *****
    # con_homework_3()

    # 遍历字典获取元素
    con_homework_4()


def con_homework_4():
    # 遍历字典获取元素
    favorite_places = {'张三': ['上海', '北京', '深圳'],
                       '李四': ['张家界', '九寨沟', '鼓浪屿']}
    name = input('请输入姓名:')
    for name_item in favorite_places.keys():
        if name_item == name:
            print(favorite_places[name])


def con_homework_3():
    line = 1
    while line < 6:
        print('*'*line)
        line += 1


def con_homework_2():

    while True:
        input_str = input('请输入1：‘剪刀’，2：‘石头’，3：‘布’。 ')
        input_int = int(input_str)
        machine_int = random.randint(1, 3)
        if machine_int == input_int:
            print('打和了,请重新输入。')
            continue

        if machine_int > input_int:
            print('你输了')
        else:
            print('你赢了')
        break


def con_homework_1():
    '''
    题目:随机输入一些成绩，利用条件运算符的嵌套学习成绩>=90分的同学用A表示，60-89分之 间的用B表示，60分以下的用C表示。
    :return:
    '''
    score_str = input('请输入成绩：')
    score = int(score_str)
    if score >= 90:
        print('A')
    elif score >= 60:
        print('B')
    else:
        print('C')


def set_homework():
    '''
    经理有:曹操，刘备，孙权 技术员:曹操，孙权，张飞，关羽 用集合求:
    1.既是经理也是技术员的有谁?
    2.是技术员但不是经理的人有谁?
    3.是经理，但不是 技术员的有谁?
    4.张飞是经理吗?
    5.身兼一职的人有谁?
    6.经理和技术员共有几人?
    :return:
    '''
    manager = {'曹操', '刘备', '孙权'}
    technician = {'曹操', '孙权', '张飞', '关羽'}
    print(f'既是经理也是技术员:{manager.intersection(technician)}')
    manager_only_set = manager.difference(technician)
    technician_only_set = technician.difference(manager)
    print(f'是技术员但不是经理:{technician_only_set}')
    print(f'是经理但不是技术员:{manager_only_set}')
    print(f'张飞是经理吗?:{"张飞" in manager}')

    only_set = manager_only_set.copy()
    only_set.update(technician_only_set)
    print(f'身兼一职的人有谁?:{ only_set }')

    total = manager.copy()
    total.update(technician)
    print(f'经理和技术员共有几人?:{len(total)}')


def practice():
    '''
    1.从键盘输入一个字符串，将小写字母全部转换成大写字母,将字符串以列表的形式输出(如果字符串包含整数,并取整)?
    2.随机输入一个正整数，要求:一、求它是几位数，二、逆序打印出各位数字。
    3.输入一行字符，分别统计出其中英文字母、空格和数字的个数。
    :return:
    '''
    # practice_1()
    # practice_2()
    practice_3()


def practice_3():
    str = input('请输入字符串')
    count_en = 0
    count_temp = 0
    count_dig = 0
    for s in str:
        count_dig += 1 if s.isdigit() else 0
        count_temp += 1 if s == ' ' else 0
        count_en += 1 if (ord(s) >= 97 and ord(s) <= 122) or (ord(s) >= 65 and ord(s) <= 90) else 0
    print(f'句子中有{count_en}个英文字母，{count_temp}个空格， {count_dig}个数字')


def practice_2():
    str = input('请输入一个正整数')
    s = str.strip()
    if len(s) < 8:
        print('这是一个%d位的数' % (len(s)))
        print(str[::-1])
    else:
        print('输入错误')


def practice_1():
    str = input('请输入字符串')
    lst = []
    for s in str:
        if s.isdecimal():
            lst.append(int(s))
        else:
            lst.append(s.upper())
    print(lst)


def tuple_homework():
    '''
    1)创建score 元组，其中包含10 个数值 (675,345,56,377,76,885,564,34,723,51);
    2)输出score 元组中第2个元素的数值;
    3)输出score 元组中第1~3 个元素的值;
    :return:
    '''
    tuple_1 = (675, 345, 56, 377, 76, 885, 564, 34, 723, 51)
    print(tuple_1[1])
    print(tuple_1[1:4])



def dict_homework():
    '''
    字典使用人名作为键，每个人用另一个字典来表示，其键”phone和”addr” 分别表示他们的联系电话和地址，重复输入5次，最后将字典打印出来。
    :return:
    '''
    person = {
        'MaoT': {'phone': 1391243, 'addr': '广东'},
        'Peter': {'phone': 17712489, 'addr': '浙江'},
        'Tom': {'phone': 1330029, 'addr': '江苏'},
        'Jerry': {'phone': 14432525, 'addr': '甘肃'},
        'Tim': {'phone': 11384745, 'addr': '云南'}
    }
    for key, value in person.items():
        phone, addr = person[key].values()
        print('name:%s, phone:%s, add:%s' % (key, phone, addr))


def base_homework():
    '''
    Python基础作业：
     1、编写一个程序输出自己的姓名和电话
     2、使用变量接收用户输入的姓名和电话，然后输出
     3、提水果店编写一个1+n的程序，n为用户输入的值
    :return:
    '''
    # 1、编写一个程序输出自己的姓名和电话
    base_1()
    # 2、使用变量接收用户输入的姓名和电话，然后输出
    base_2()
    # 3、提水果店编写一个1+n的程序，n为用户输入的值
    base_3()


def base_3():
    while True:
        num = input('请输入数字：')
        if num.isdigit():
            num = int(num)
            if num < 0:
                print('数字小于0')
                exit(-1)
            else:
                print(sum(range(num+1)))
        else:
            print('输入非法。')
            exit(-1)


def base_2():
    name = input('请输入您的姓名：')
    phone_num = input('请输入你的电话号码：')
    print('Your name is %s, your phone number is %s' % (name, phone_num))


def base_1():
    name = 'Tenglei'
    phone_num = '19969252064'
    print('My name is %s, my phone number is %s' % (name, phone_num))


def str_homework():
    '''
    字符串作业：
    1.定义一个字符串，计算一个字符串的长度，及字母、数字出现的次数.
    2.从键盘输入一个字符串，将小写字母全部转换成大写字母
    3.替换一个字符串中的一个单词
    :return:
    '''
    # 1.定义一个字符串，计算一个字符串的长度，及字母、数字出现的次数.
    str_1()
    # 2.从键盘输入一个字符串，将小写字母全部转换成大写字母
    str_2()
    # 3.替换一个字符串中的一个单词
    str_3()


def str_1():
    str1 = 'a2c7asdf82qvd8'
    num_count = 0
    alpha_count = 0
    for i in str1:
        num_count += 1 if i.isalpha() else 0
        alpha_count += 1 if i.isdigit() else 0
    print(f"字符串长度：{len(str1)}，字母：{num_count}个，数字：{alpha_count}个")


def str_2():
    input_str = input()
    print(input_str.upper())


def str_3():
    str = 'hello tl, how do you do'
    str_replace = str.replace('do', 'DO', 1)
    print(str_replace)


if __name__ == '__main__':
    main()