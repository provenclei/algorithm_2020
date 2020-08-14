# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  DataProcessing.py
@Description    :  
@CreateTime     :  2020/4/27 22:13
------------------------------------
@ModifyTime     :  
"""
import csv
import json
import pickle
import xlrd
import xlwt


# 定义一个存储的对象
class DataProcessing(object):
    def __init__(self, name='pickle', num=10):
        super().__init__()
        self.name = name
        self.num = num

    def add(self, num):
        return num + self.num


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


def main():
    handle_1 = read_write_handle('./doc/txt_file.txt', 'read')()
    for i in range(5):
        print(next(handle_1))

    print('*'*20)
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
    obj_data = DataProcessing('mix', 99)
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


if __name__ == '__main__':
    main()