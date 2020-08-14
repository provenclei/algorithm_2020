# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  作业(3.8).py
@Description    :  
@CreateTime     :  2020/4/25 21:21
------------------------------------
@ModifyTime     :
作业4：a=np.arange(6).reshape((3,2))，把a的输出变成[[0,3],[1,4],[2,5]]。
作业5：挖掘文件（./doc/data.txt）公司的全称和简称。
"""
import numpy as np
import re

patten = re.compile(r'(?P<qc>.*)（.*简称(?P<jc>.*)）')


def homework_4():
    '''
    a=np.arange(6).reshape((3,2))，把a的输出变成[[0,3],[1,4],[2,5]]。
    :return:
    '''
    a = np.arange(6).reshape((3, 2))
    print(a)


def mining_named_recognization(input_f, output_f):
    '''
    挖掘文件（./doc/data.txt）公司的全称和简称。
    :param input_f:
    :param output_f:
    :return:
    '''
    with open(input_f, 'r', encoding='utf-8') as fi, open(output_f, 'a+', encoding='utf-8') as fo:
        for line in fi:
            if not line.strip():
                continue
            re_lst = patten.findall(line)
            if len(re_lst) != 0:
                fo.write(str(re_lst) + '\n')


def main():
    # homework_4()
    # 作业5
    mining_named_recognization('./doc/data.txt', './doc/recognization.txt')


if __name__ == '__main__':
    main()