# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/18 22:14
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：局部和全局变量
"""
b = 2


def func():
    global b   #这样就可以使全局变量b在内部被改变
    # 这是一个局部变量
    a = 1
    b = 3
    print(a)


func()
print(b)
