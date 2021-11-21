# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/11 21:07
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：元组
"""
# 空列表
a = []

# 空元组
a = ()
print(type(a))
# 一个值元组
a = (1,)
print(type(a))

# 一个元组定义好了之后，不让更改里面的任意值（包括增加，删除，修改）
t = (1,2,3)
print(t[1])

# 截取和拼接，不算更改，它重新获得了一个元组
ta = t + a
print(ta)
print(id(t))
print(id(ta))

# 当某一组数据，你不希望被程序更改的时候，就可以使用元组，为了安全性考虑

# 元组和列表是可以互转的
# 元组转列表
list_ta = list(ta)
print(list_ta)
# 列表转元组
print(tuple(list_ta))





