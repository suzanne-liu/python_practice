# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/29 11:35 下午
@Function ：边牧犬_继承
"""
from Class_practice.class06.class_dog import Dog


class bianmu(Dog):
    """设置子类的类变量"""
    mao = "长毛"

    """子类构造函数"""

    def __init__(self, skin):
        """必须调用父类的构造函数"""
        Dog.__init__(self, skin)
        """重写name默认值"""
        self.name = "小牧羊犬"

        """设置一些子类特有的实例变量"""
        self.texing = "耐寒"

    def say(self, s):
        """重写叫声"""
        print(self.name + "的叫声是"+s)

    """类函数"""
    @classmethod
    def set_eye(cls, e):
        cls.eye = e
        print(cls.eye)

    """扩展新实例函数"""
    def jineng(self):
        print(self.name + "会牧羊")


if __name__ == '__main__':
    """实例化一个牧羊犬叫小白"""
    xiaobai = bianmu("白色")
    xiaobai.set_name("小白")
    xiaobai.say("汪汪汪汪")
    """继承类变量"""
    print(xiaobai.eye)

    print(xiaobai.texing)
    xiaobai.jineng()

    xiaobai.set_eye(5)

