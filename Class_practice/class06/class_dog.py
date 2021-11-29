# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/29 9:49 下午
@Function ：Dog 类
"""


class Dog:
    # 类变量
    eye = 2

    # 初始化构造函数,这里设置skin和name，其中skin需要传参
    def __init__(self, skin="土黄"):
        # 初始化实例默认值,创建实例时必定要使用，self代表实例，需要调用实例进行赋值
        self.skin = skin  # 接收传入的参数
        self.name = "狗"
        print(self.skin)
        print(self.name)

    # 创建非默认构造函数的实例函数
    def say(self, s):
        """小狗的叫声"""
        print(self.name + "的叫声是：" + s)

    def set_name(self, n):
        self.name = n

    # 创建类函数,cls指的是类本身
    # 这个装饰器的作用：标识为类函数，如果没有这个装饰器，就不是
    @classmethod
    def set_eye(cls, e):
        cls.eye = e
        print(cls.eye)


if __name__ == '__main__':
    # 使用类创建一个实例
    jinmao = Dog("金色")

    # 调用类变量
    print("dog.eye : " + str(Dog.eye))
    print("jinmao.eye : " + str(jinmao.eye))

    # 调用实例函数
    jinmao.set_name("小金毛")
    jinmao.say("呜呜呜")

    # 修改类变量
    jinmao.set_eye(3)
    Dog.set_eye(4)