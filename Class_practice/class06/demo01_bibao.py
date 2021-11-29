# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/18 20:19
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：闭包
"""


# def func():
#     print(a)
#
#
# # python是一门解释型编程语言
# if False:
#     a = 1
#
# func()


def outer():
    def inter():
        print(b)
        print(c)

    # b这个变量是在inter之后定义的
    b = 1
    c = 2
    return inter()     # 表示这时候才去调用inter，解决一些闭包调用问题

outer()


