# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/11 21:26
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：字典
"""
# 列表存所有名字
names = ['ok1', '177', '173', '奇幻', '173', 'RoseMary']
"""
我还要存每一位学员上课时间，而且我想要快速获取到某一位学员的上课时间
方式1：再用一个列表存时间，一一对应
方式2：使用字典
"""
# 空字典
stu_dict = {}
stu_dict = {'ok1': 60, '177': 66, '173': 67, '奇幻': 60, 'RoseMary': 65}
# 通过键获取值
print(stu_dict.get('RoseMary'))
print(stu_dict['RoseMary'])
# 区别（只体现在字典里面没有这个键的时候）
# 第一种获取到None
print(stu_dict.get('RoseMary1'))
# 第二种方式会报错
# print(stu_dict['RoseMary1'])

# 键值对数量
print(len(stu_dict))

# 修改值
stu_dict['RoseMary'] = 66
print(stu_dict)
# 更新的方式，如果键不存在就新增键值对，键存在就是更新值
stu_dict['RoseMary2'] = 66
print(stu_dict)

# 删除减值对，都是通过键来删除
stu_dict.pop('RoseMary2')
print(stu_dict)
del stu_dict['ok1']
print(stu_dict)

# 清空（字典和列表都可以clear）
names.clear()
stu_dict.clear()
print(names)
print(stu_dict)

# False对应（空列表，空元组，空字典）（也都不参与遍历）
b = bool(stu_dict)
print(b)

# 字典的键和值都可以看作是列表
stu_dict = {'ok1': 60, '177': 66, '173': 67, '奇幻': 60, 'RoseMary': 65}
print(list(stu_dict.keys()))
print(list(stu_dict.values()))

# items的遍历
print(stu_dict.items())
# 当遍历的时候，如果元素是一个列表或者元组，你可以用多个变量直接对应位置元素
for key, value in stu_dict.items():
    print('%s=%s' % (key, value))
    print('{}={}'.format(key, value))

for item in stu_dict.items():
    print(item)

# 遍历键获取值
for key in stu_dict.keys():
    print(stu_dict.get(key))

# 可以直接遍历值
for value in stu_dict.values():
    print(value)
