# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 21:09
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：函数的传值与传地址
"""

# a = 1
#
#
# def func1(b):
#     # 接收的参数叫形参
#     print(id(b))
#     b = 2
#     print(id(b))
#     print('函数里面',b)
#
#
# # 传递的参数叫实参，实参和形参不是一个参数
# # 这种形式就叫传值
# func1(a)
# print(id(a))
# print('函数外面',a)

# 传地址

myl1 = [1,2,3,4]


def func2(myl2):
    # 不能改变容器变量本身，否则就不能传地址
    # myl2 = [11,22]
    myl2[1] = 3
    print(myl2)


# 传地址：改变容器里面指针指向值（这时候，函数内外都会一起变）
func2(myl1)
print(myl1)



