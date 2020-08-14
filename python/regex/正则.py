# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  正则.py
@Description    :  
@CreateTime     :  2020/4/29 15:28
------------------------------------
@ModifyTime     :  
"""
import re


def main():
    # match：从其实位置开始匹配，未匹配到返回 None
    match = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello tengeli!')
    print("m.string:", match.string)
    print("m.re:", match.re)
    print("m.pos:", match.pos)
    print("m.endpos:", match.endpos)
    print("m.lastindex:", match.lastindex)
    print("m.lastgroup:", match.lastgroup)

    print("m.group(1,2):", match.group(1, 2))
    print("m.groups():", match.groups())
    print("m.groupdict():", match.groupdict())
    print("m.start(2):", match.start(2))
    print("m.end(2):", match.end(2))
    print("m.span(2):", match.span(2))
    print(r"m.expand(r'\2 \1\3'):", match.expand(r'\2 \1\3'))

    # re.searh 扫描整个字符串并返回第一个成功的匹配。
    print(re.search('www', 'www.runoob.com.www').span())  # 在起始位置匹配
    print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
    line = "Cats are smarter than dogs"
    # re.S: 使 . 匹配包括换行在内的所有字符
    # re.M: 多行匹配，影响 ^ 和 $
    # re.I: 使匹配对大小写不敏感
    searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
    if searchObj:
        print("searchObj.group() : ", searchObj.group())
        print("searchObj.group(1) : ", searchObj.group(1))
        print("searchObj.group(2) : ", searchObj.group(2))
    else:
        print("Nothing found!!")

    # re.findall 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
    # match 和 search 是匹配一次,findall 匹配所有。
    pattern = re.compile(r'\d+')  # 查找数字
    result1 = pattern.findall('runoob 123 google 456')
    result2 = pattern.findall('run88oob123google456', 0, 10)
    print(result1, result1.index('456'))
    print(result2)


if __name__ == '__main__':
    main()