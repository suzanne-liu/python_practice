# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/18 20:14
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：希望自己写的每一个排序函数提供花了多长时间的功能
    装饰器的应用
"""
import time


def timer(t='s'):
    """
    给函数提供执行时间统计的装饰器
    :param t: 时间的单位，默认是s
    """
    def outer(func):
        def wrapper(*args,**kwargs):
            # 执行函数前记录开始时间
            start_time = time.time()
            # 执行函数
            res = func(*args,**kwargs)
            # 记录结束时间，并打印耗时
            end_time = time.time()
            print(func.__name__ + "的耗时为：" + str(end_time - start_time))
            return res
        return wrapper
    return outer

