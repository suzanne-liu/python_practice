# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/11 20:12
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：变量
"""

# a是一个变量，3是一个数据值
# a是一个指针，指向3所在的内存空间
# 通过初始化定义
a = 3
print(id(3))
print(id(a))
a = '4'
print(id(a))
b = 3
print(id(b))

# 以字母开始的字符串（一般只包含字母数字，下划线）
a_3 = 4
# 变量使用：使用变量的值或者改变变量的值
# 使用值
print(a)
# 改变值
a = 44
print(a)

