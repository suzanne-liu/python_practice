# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/27 1:28 下午
@Function ：请输入模块功能描述
"""
import time
from Class_practice.Sort import *

s = [166, 167, 155, 180, 177, 160, 178, 169, 155, 172]

t1=time.time()
quick_sort.quick_sort(s)
print(s)
t2=time.time()
t=t2-t1
