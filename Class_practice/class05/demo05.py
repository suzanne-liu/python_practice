# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 21:47
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：递归
"""


# n! = n*(n-1)!，1！= 1
def func1(n):
    """n的阶乘"""
    # 出口：1！= 1
    if n == 1:
        return 1

    # n! = n*(n-1)!
    jiec = n * func1(n-1)
    return jiec


print(func1(10))

