# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/11 20:19
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：列表
"""
# 统计来上课的所有学员的名字
name1 = 'ok'
name2 = '177'
name3 = '173'

# 我们可以使用线性顺序的有限序列来存储
names = ['ok', '177', '173', '173']

# 获取元素值
# 下标：列表每一个元素的序号（从0开始）
print(names[1])

# 一共有多少元素（列表长度）
print(len(names))

# 更新某个元素值（给对应元素赋值）
names[0] = 'ok1'
print(names)

# 添加元素
# 在末尾添加
names.append('RoseMary')
print(names)
# 在指定位置前面插入一个元素
names.insert(3, '奇幻')
print(names)
# 删除
# 通过下标删除
del names[0]
print(names)
# 通过元素值删除（从左到右，删除第一个值）
names.remove('173')
print(names)

# 列表的拼接
# 字符串你可以看作是一个字符列表
my_list1 = ['1', '3']
my_list2 = ['2', '4']
print(my_list1 + my_list2)
# 你可以把s1看做是一个这样的列表['a','b']
s1 = 'ab'
s2 = 'cd'
print(s1 + s2)

# 乘法，对列表自己进行n次拼接（负数等同于0）
print(my_list1 * 3)

# 列表的截取
my_l = [0, 1, 2, 3, 4, 5, 6, 7, 8, '9']
"""
截取my_l[start:end:step]
左闭右开的区间
step：步长，默认是1
"""
# 左闭右开
print(my_l[1:4])
# step：步长
print(my_l[1:9:2])
# 当步长为-1，倒过来
print(my_l[9::-1])
"""
start和end不写的情况
当step为正数：start不填代表从0开始，end不填代表到末尾
当step为负数：start不填代表len(my_l)-1，end不填代表下标的起始位置
"""
print(my_l[:3])
print(my_l[3:])

print(my_l[::-1])
print(my_l[len(my_l)-1::-1])

# 字符串的反转
a = 'dcba'
print(a[::-1])

# 需求：我想要把学员名字都标识为VIP学员，例如（VIP_ok）
"""
分析：实现这个功能，我只能一个个取修改列表里面所有的元素
['ok1', '177', '173', '奇幻', '173', 'RoseMary']
"""

stu = ['ok1', '177', '173', '奇幻', '173', 'RoseMary']
print(len(stu))
# 这就叫列表的遍历（下标遍历：你可以同时读取值，修改值）
for i in range(0,len(stu)):
    stu[i] = 'VIP_' + stu[i]

print(stu)

# 成员遍历（只能读取值）
for s in stu:
    s += 'aaa'

print(stu)


# stu = ['ok1', '177', '173', '奇幻', '173', 'RoseMary']
# # 倒着取
# print(stu[-1])
# # 下标越界
# for i in range(0,6):
#     stu[i] = 'VIP_' + stu[i]
#     # 一定不要在遍历的删除
#     if i == 2:
#         stu.remove('VIP_ok1')
#
# print(stu)