# -*- coding: utf-8 -*-
"""
@Author         :  LEITENG
@Version        :  
------------------------------------
@File           :  魔术方法.py
@Description    :  
@CreateTime     :  2020/4/26 17:59
------------------------------------
@ModifyTime     :  魔术方法就是一个类/对象中的方法，和普通方法唯一的不同时，普通方法需 要调用!而魔术方法是在特定时刻自动触发。

用于比较的魔术方法:
    __cmp__(self, other) 是比较方法里面最基本的的魔法方法
    __eq__(self, other) 定义相等符号的行为，==
    __ne__(self,other) 定义不等符号的行为，!=
    __lt__(self,other) 定义小于符号的行为，<
    __gt__(self,other) 定义大于符号的行为，>
    __le__(self,other) 定义小于等于符号的行为，<=
    __ge__(self,other) 定义大于等于符号的行为，>=

基本的魔法方法：
    __new__(cls[, ...]) 是在一个对象实例化的时候所调用的第一个方法
    __init__(self[, ...]) 构造器，当一个实例被创建的时候调用的初始化方法
    __del__(self ) 析构器，当一个实例被销毁的时候调用的方法
    __call__(self[, args...]) 允许一个类的实例像函数一样被调用:x(a, b) 调用 x.__call__(a, b)
    __len__(self ) 定义当被 len() 调用时的行为

属性相关：
    __getattr__(self, name) 定义当用户试图获取一个不存在的属性时的行为
    __getattribute__(self, name) 定义当该类的属性被访问时的行为
    __setattr__(self, name, value) 定义当一个属性被设置时的行为
    __delattr__(self, name) 定义当一个属性被删除时的行为
    __dir__(self ) 定义当 dir() 被调用时的行为
    __set__(self, instance, value) 定义当描述符的值被改变时的行为
    __delete__(self, instance) 定义当描述符的值被删除时的行为
    __get__(self, instance, owner) 定义当描述符的值被取得时的行为

单目运算符和函数：
    __pos__(self ) 实现一个取正数的操作
    __neg__(self ) 实现一个取负数数的操作
    __abs__(self ) 实现一个内建的 abs() 行为
    __invert__(self) 实现一个取反操作符(~操作符)的行为
    __round__(self, n) 实现一个内建的round()函数的行为
    __floor__(self) 实现math.floor()的函数行为
    __ceil__(self ) 实现math.ceil()的函数行为
    __trunc__(self) 实现math.trunc()的函数行为

双目运算符或函数：
    __add__(self, other) 实现一个加法
    __sub__(self, other) 实现一个减法
    __mul__(self, other) 实现一个乘法
    __floordiv__(self, other) 实现一个“//”操作符产生的整除操作()
    __div__(self, other) 实现一个“/”操作符代表的除法操作
    __truediv__(self, other) 实现真实除法
    __mod__(self, other) 实现一个“%”操作符代表的取模操作
    __divmod__(self, other) 实现一个内建函数divmod()
    __pow__ 实现一个指数操作(“**”操作符)的行为
    __lshift__(self, other) 实现一个位左移操作(<<)的功能
    __rshift__(self, other) 实现一个位右移操作(>>)的功能
    __and__(self, other) 实现一个按位进行与操作(&)的行为
    __or__(self, other) 实现一个按位进行或操作的行为
    __xor__(self, other)  实现一个按位进行异或操作的行为

增量运算：
    __iadd__(self, other) 加法赋值
    __isub__(self, other) 减法赋值
    __imul__(self, other) 乘法赋值
    __ifloordiv__(self, other) 整除赋值，地板除，相当于 //= 运算符
    __idiv__(self, other) 除法赋值，相当于 /= 运算符
    __itruediv__(self, other) 真除赋值
    __imod_(self, other) 模赋值，相当于 %= 运算符
    __ipow__ 乘方赋值，相当于 **= 运算符
    __ilshift__(self, other) 左移赋值，相当于 <<= 运算符
    __irshift__(self, other)  右移赋值，相当于 >>= 运算符
    __iand__(self, other) 与赋值，相当于 &= 运算符
    __ior__(self, other) 或赋值
    __ixor__(self, other) 异或运算符，相当于 ^= 运算符

类型转换：
    __int__(self ) 转换成整型
    __long__(self ) 转换成长整型
    __float__(self) 转换成浮点型
    __complex__(self) 转换成 复数型
    __oct__(self ) 转换成八进制
    __hex__(self ) 转换成十六进制
    __index__(self) 如果你定义了一个可能被用来做切片操作的数值型，你就应该定义 __index__
    __trunc__(self) 当 math.trunc(self) 使用时被调用__trunc__返回自身类型的整型截取
    __coerce__(self, other) 执行混合类型的运算

容器类型：
    __len__(self) 定义当被 len() 调用时的行为(返回容器中元素的个数)
    __getitem__(self, key) 定义获取容器中指定元素的行为，相当于 self[key]
    __setitem__(self, key, value) 定义设置容器中指定元素的行为，相当于 self[key] = value
    __delitem__(self, key) 定义删除容器中指定元素的行为，相当于 del self[key]
    __iter__(self) 定义当迭代容器中的元素的行为
    __reversed__(self) 定义当被 reversed() 调用时的行为
    __contains__(self, item) 定义当使用成员测试运算符(in 或 not in)时的行为

其他：
    __repr__(self ) 定义当被 repr() 调用时的行为
    __str__(self ) 定义当被 str() 调用时的行为
    __bytes__(self ) 定义当被 bytes() 调用时的行为
    __hash__(self ) 定义当被 hash() 调用时的行为
    __bool__(self ) 定义当被 bool() 调用时的行为，应该返回 True 或 False
    __format__(self, format_spec) 定义当被 format() 调用时的行为
"""


class Magic(object):
    def __init__(self):
        self.name = 'magic'
        self.num = 1
        self.b = 3
        self.l = [1, 2, 3, 4, 5, 6]

    def __call__(self,a,b):
        c = a + b
        return c

    def __getitem__(self, index):
        return self.l[index]

    def __len__(self):
        return len(self.l)


def main():
    m = Magic()
    # 调用 __call__
    s = m(1, 2)
    # 调用 __getitem__
    s1 = m[1]
    # 调用 __len__
    l = m.__len__()  # len(m)
    print(l)


if __name__ == '__main__':
    main()