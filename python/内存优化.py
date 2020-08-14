# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  内存优化.py
@Description    :  
@CreateTime     :  2020/4/26 09:40
------------------------------------
@ModifyTime     :  
"""
# 所有字母（无论大小写）
from string import ascii_letters
# 内存调试工具
from pympler.asizeof import asizesof


def slots_memory(num=0):
    attrs = list(ascii_letters[:num])

    class Unslotted(object):
        pass

    class Slotted(object):
        __slots__ = attrs

    unslotted = Unslotted()
    slotted = Slotted()
    for attr in attrs:
        unslotted.__dict__[attr] = 0
    exec('slotted.%s = 0' % attr, globals(), locals())
    memory_use = asizesof(slotted, unslotted, unslotted.__dict__)
    return memory_use


def slots_test(nums):
    return [slots_memory(num) for num in nums]


def main():
    nums = []
    slots_test(nums)


if __name__ == '__main__':
    main()