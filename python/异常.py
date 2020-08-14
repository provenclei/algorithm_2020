# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  异常.py
@Description    :  
@CreateTime     :  2020/4/28 21:44
------------------------------------
@ModifyTime     :  
"""


def open_file(input='a.txt', mode='r', encoding='utf8'):
    d = {'a': 1, 'b': 2}
    try:
        c = d['c']
        with open(input,mode, encoding=encoding) as fi:
            for line in fi:
                print(line)
    except FileNotFoundError:
        print(f"{input} is not exist !!!")
    except KeyError:
        print(f"dict d not key c !!!")
    finally:
        try:
            with open(input,mode,encoding=encoding) as fi:
                for line in fi:
                    print(line)
                # fi.close()
        except:
            print(f"{input} is not exist !!!")
        a, b = 1, 2
        c = a+b
        print(c)


def main():
    open_file(input='a.txt', mode='r', encoding='utf8')


if __name__ == '__main__':
    main()