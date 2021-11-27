# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 21:34
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：导入
"""
# # 函数导入
# from class05.demo1 import my_replace
#
# s = my_replace('abcdabcdabcdabcdabcd','ab','cd',3)
# print(s)

# # 模块导入
# from class05 import demo1
# s = demo1.my_replace('abcdabcdabcdabcdabcd','ab','cd',3)
# print(s)

# 模糊导入（针对模块导入）,需要在__init__.py中先定义好all代表什么
from class05 import *

# s = demo1.my_replace('abcdabcdabcdabcdabcd','ab','cd',3)
# print(s)
#
# import aaa
#
# aaa.test()