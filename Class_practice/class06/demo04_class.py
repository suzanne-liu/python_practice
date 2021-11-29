# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/18 21:16
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：人类
"""


class Human:
    # 写在类名里面，函数体之外的都叫类变量
    # 有两只眼睛
    eye = 2
    name1 = 'aaa'

    def __init__(self,skin='黄色'):
        """
        构造函数（编程角度来看是为了初始化数据）
        通过类名调用
        """
        self.skin = skin
        self.name = '小宝宝'

    def say(self,s):
        """会说话"""
        print(self.name + s)

    def set_name(self,n):
        """
        给人取名字
        :param n: 名字
        """
        self.name = n

    @classmethod
    def set_eye(cls,e):
        """设置类变量"""
        cls.eye = e




if __name__ == '__main__':
    # 类变量用类名调用
    Human.eye = 3
    print(Human.eye)
    # 创建一个对象（这个人生下来了）
    will = Human('黄色')
    will.set_name('will')
    will.say('开始哭')

    suzan = Human("哈哈哈哈哦哦哦")
    suzan.say("o ")
    print("suzan skin:"+suzan.skin)


    vai = Human('黑色')
    vai.name = 'vai'
    vai.say('哈哈大笑')
    print(vai.skin)
    print(will.name)
