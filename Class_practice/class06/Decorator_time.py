# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/30 12:15 上午
@Function ：函数执行统计装饰器
"""
import time


def sumtime():
    def outer(func):
        def wapper(*args, **kwargs):
            start_time = time.time()
            print("开始时间：" + str(start_time))

            res = func(*args, **kwargs)

            end_time = time.time()
            print("结束时间：" + str(end_time))

            sum_time = end_time - start_time
            print(func.__name__+"执行时间总和为："+str(sum_time))

            """注意返回的是函数执行结果"""
            """装饰器中一定要调用函数，一定要返回函数的执行结果，可以把装饰器想成在函数外面罩一个罩子"""
            return res

        return wapper

    return outer
