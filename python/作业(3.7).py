# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  作业(3.7).py
@Description    :  
@CreateTime     :  2020/4/25 21:20
------------------------------------
@ModifyTime     :
作业1、
用装饰器实现任意函数计时和函数峰值内存使用的统计

作业2、
骰子:
模块random 包含以各种方式生成随机数的函数，其中的randint()返回 一个位于指定范围内的整数，
例如，下面的代码返回一个1~6 内的整数:
    from random import randint
    x = randint(1, 6)
请创建一个Die 类，它包含一个名为sides的属性,该属性的默认值为6。编写一个名为roll_die()的方法，
它打印位于1 和骰子面数之间的随机数。
创建一个6 面的骰子，再掷10 次。

作业3、
采用闭包的形式（或者其他简练（代码量要少）的形式）编写一个程序，它能够读写txt,json,csv,docx,excel,pkl格式的文件。
"""
from random import randint
import csv
import json
import pickle
import time
import psutil
import xlrd
import xlwt


def cal_time(func):
    def inner_fun(*args, **kwargs):
        star_time = time.time()
        result = func(*args, **kwargs)
        print(f"运行函数:{func.__name__}")
        end_time = time.time()
        print(f"运行时间为:{end_time - star_time}")
        return result
    return inner_fun


def cal_memory(func):
    def inner_fun(*args, **kwargs):
        memory = psutil.virtual_memory()
        total = float(memory.total)
        result = func(*args, **kwargs)
        print(f"计算函数内存:{func.__name__}")
        used = float(memory.used)
        print(f"总内存：{total}---已使用内存：{used}")
        return result
    return inner_fun


@cal_memory
@cal_time
def add(num):
    return sum(i for i in range(1, num+1))


def home_work_1():
    '''
    作业1、
    用装饰器实现任意函数计时和函数峰值内存使用的统计
    :return:
    '''
    print(add(1000))


class Die(object):
    # 默认值
    sides = 6

    def roll_die(self):
        # 骰子面
        self.sides = randint(1,6)
        # 生成随机数
        return randint(1, self.sides)


def home_work_2():
    '''
    作业2、
    骰子:
    模块random 包含以各种方式生成随机数的函数，其中的randint()返回 一个位于指定范围内的整数，
    例如，下面的代码返回一个1~6 内的整数:
        from random import randint
        x = randint(1, 6)
    请创建一个Die 类，它包含一个名为sides的属性,该属性的默认值为6。编写一个名为roll_die()的方法，
    它打印位于1 和骰子面数之间的随机数。
    创建一个6 面的骰子，再掷10 次。
    :return:
    '''
    d = Die()
    for i in range(1, 11):
        side = d.roll_die()
        print(f'第{i}次生成骰子点数：{side}')


def read_write_handle(path, method='read'):
    '''
    使用闭包实现处理不同格式（txt,pkl,csv,json）文件（读写）的方法
    :param path: 路径
    :param method: 方法
    :return:
    '''

    def read_write_handle(path, method='read'):
        '''
        使用闭包实现处理不同格式（txt,pkl,csv,json）文件（读写）的方法
        :param path: 路径
        :param method: 方法
        :return:
        '''
        assert method in ('read', 'write'), 'method is error'
        f_tail = path.split('.')[-1]

        def txt_read():
            with open(path, 'r', encoding='utf-8') as f:
                print("txt文件正在读取中。。。")
                for line in f:
                    yield line.strip()

        def pkl_read():
            with open(path, 'rb') as f:
                print("pkl文件正在读取中。。。")
                return pickle.load(f)

        def csv_read():
            with open(path, 'rt', encoding='utf-8') as f:
                print("csv文件正在读取中。。。")
                reader = csv.reader(f)
                for line in reader:
                    yield line

        def json_read():
            with open(path, 'r') as f:
                print("json文件正在读取中。。。")
                reader = f.read()
                data_json = json.loads(reader)
                return data_json

        def xls_read(table_name):
            word_book = xlrd.open_workbook(path)
            print(f'总共{word_book.nsheets}张表')
            table = word_book.sheet_by_name(table_name)
            # cols = table.ncols
            rows = table.nrows
            row_lst = []
            print("xls文件正在读取中。。。")
            for i in range(0, rows):
                row_data = table.row_values(i)
                row_lst.append(row_data)
            return row_lst

        def txt_write(data):
            with open(path, mode='w', encoding='utf-8') as f:
                print("txt文件正在写入中。。。")
                f.write(data)

        def pkl_write(data):
            with open(path, mode='wb') as f:
                print("pkl文件正在写入中。。。")
                pickle.dump(data, f)

        def csv_write(headline, rows):
            with open(path, mode='w', newline='') as f:
                print("csv文件正在写入中。。。")
                writer = csv.writer(f, dialect='excel')
                writer.writerow(headline)
                writer.writerows(rows)

        def json_write(data):
            with open(path, mode='w', encoding='utf-8') as f:
                print("json文件正在写入中。。。")
                json.dump(data, f)

        def xls_write(data):
            word_book = xlwt.Workbook()
            sheet = word_book.add_sheet('Sheet1')
            # xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')   # 数据格式
            # style = xlwt.XFStyle()  # 初始化样式
            # font = xlwt.Font()  # 为样式创建字体
            # font.name = 'Times New Roman'
            # font.bold = True  # 黑体
            # font.underline = True  # 下划线
            # font.italic = True  # 斜体字
            # style.font = font  # 设定样式
            print("excel文件正在写入中。。。")
            for i, items in enumerate(data):
                for j, item in enumerate(items):
                    sheet.write(i, j, item)
            word_book.save(path)

        # route = {
        #     'read': {'txt': txt_read, 'pkl': pkl_read, 'csv': csv_read, 'json': json_read, 'xls': xls_read},
        #     'write': {'txt': txt_write, 'pkl': pkl_write, 'csv': csv_write, 'json': json_write, 'xls': xls_write}
        #          }
        # return route[method][f_tail]

        return eval(f_tail + '_' + method)


def home_work_3():
    '''
    作业3、
    采用闭包的形式（或者其他简练（代码量要少）的形式）编写一个程序，它能够读写txt,json,csv,docx,excel,pkl格式的文件。'''
    handle_1 = read_write_handle('./doc/txt_file.txt', 'read')()
    for i in range(5):
        print(next(handle_1))

    print('*' * 20)
    handle_2 = read_write_handle('./doc/test.pkl', 'read')()
    print(handle_2)

    print('*' * 20)
    handle_3 = read_write_handle('./doc/titanic.csv', 'read')()
    for i in range(5):
        print(next(handle_3))

    print('*' * 20)
    handle_4 = read_write_handle('./doc/json_data.json', 'read')
    read_handle_4 = handle_4()
    print(read_handle_4)

    print('*' * 20)
    handle_5 = read_write_handle('./doc/e.xls', 'read')
    read_handle_5 = handle_5('Sheet2')
    print(read_handle_5)

    print('*' * 20)
    handle_out_1 = read_write_handle('./doc/a.txt', 'write')
    handle_out_1('写入的文件内容：爱的沙发沙发的范德萨发')

    print('*' * 20)
    obj_data = Die()
    handle_out_2 = read_write_handle('./doc/b.pkl', 'write')
    # 写入对象
    handle_out_2(obj_data)

    print('*' * 20)
    csv_data = [['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin',
                 'Embarked'],
                ['1', '0', '3', 'Braund, Mr. Owen Harris', 'male', '22', '1', '0', 'A/5 21171', '7.25', '', 'S']]
    handle_out_3 = read_write_handle('./doc/c.csv', 'write')
    headline = csv_data[0]
    rows = [csv_data[1]]
    handle_out_3(headline, rows)

    print('*' * 20)
    json_data = {"code": 0, "data": [{"username": "Doe", "city": "13586456", "sign": "center"}]}
    handle_out_4 = read_write_handle('./doc/d.json', 'write')
    handle_out_4(json_data)

    print('*' * 20)
    xls_data = [[10, 20, 30], ['aa', 'ab', 'ac']]
    handle_out_5 = read_write_handle('./doc/e.xls', 'write')
    handle_out_5(xls_data)


def main():
    home_work_1()
    # home_work_2()
    # home_work_3()


if __name__ == '__main__':
    main()