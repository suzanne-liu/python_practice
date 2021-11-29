# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/18 21:51
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：继承
"""
from class06.demo4 import Human


class Man(Human):
    """男人类"""
    eye = 1

    def __init__(self,skin):
        """你必须在构造函数里面显示调用父类的构造函数"""
        Human.__init__(self,skin)
        # super().__init__(skin)    # 这个也表示显示调用父类的构造函数，super是关键字 代表父类
        # super(Man, self).__init__(skin)      # 这个也表示显示调用父类的构造函数，super是关键字 代表父类
        self.__money = 0

    def basketball(self):
        """拓展：男人打篮球"""
        print(self.name + '在打篮球')

    def say(self):
        """重写：只要函数名一样就是重写"""
        print('男人说话都很大声')
        self.__movie()
        self.__money = 100

    def __movie(self):
        """私有：只允许在类里面使用"""
        print('看小电影')




will = Man('黄色')
will.say()
print(will.__doc__)
print(will.say.__doc__)
print(will.say.__name__)
