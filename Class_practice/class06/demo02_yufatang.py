# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/18 20:30
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：@语法糖
"""


def my_dec(t='s'):
    """
    用来接收装饰器本身的参数
    :param t: 装饰器本身功能实现的参数
    :return:
    """
    print(t)

    def outer(func):
        """
        把被装饰的函数作为装饰器的参数传入
        :param func: 被装饰的函数
        :return: 调用闭包
        """
        print(func.__name__)

        def inter(*args, **kwargs):  # 不定长传参，这样可以接收所有参数，这样就可以装饰所有函数
            print(args)
            print(kwargs)
            print('开始执行被装饰函数')
            # 如果在装饰器里面你不调函数，是不会执行函数本身的
            res = func(*args, **kwargs)  # 不定长传参，这样可以接收所有参数
            print('被装饰函数执行完成')
            # 返回被装饰函数的返回值
            return res

        return inter

    return outer


@my_dec(t='ms')
def test(a, b=1):
    """测试函数"""
    print(a + b)
    return 1111


@my_dec
def ffff(a, b, c, d):
    print(a, b, c, d)


print(test(1, b=5))
# ffff(1,2,3,4)


# 递归不太好使用装饰器