# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/14 20:07
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：字符串处理
"""

#
# # 把url格式的参数处理为字典
# params = "query=175.10.88.71&co=&resource_id=5809&t=1636891686668&ie=utf8" \
#          "&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu&" \
#          "cb=jQuery110207174565008267173_1636891669991&_=1636891669996"
#
# # split方法：字符串切割，一某个字符或者子串为标准，把字符串切割成很多小块
# params_list = params.split('&')
# print(params_list)
# # 可以继续切割，你也可以截取
# params_dict = {}
# for s in params_list:
#     one_param = s.split('=')
#     # print(one_param)
#     # 列表里面第一个元素是键，第二个是值
#     params_dict[one_param[0]] = one_param[1]
#
# print(params_dict)

# # replace(old,new,count=-1)：把字符串里面的子串，替换为新的字符串
# s = "will，roy，tufei，will，roy，will，roy，will，roy，will，roy，will，roy，will，roy，will，roy，will，roy，will"
# # 把所有的will替换为youmi
# # count默认是-1，替换全部
# s1 = s.replace('will','youmi')
# print(s1)
# # 把第一个will替换为youmi
# s1 = s.replace('will','youmi',1)
# print(s1)
# # 把最后一个will替换为youmi
# # 先反转过来
# s1 = s[::-1]
# print(s1)
# # 我们把第一个lliw,替换为imuoy
# s1 = s1.replace('lliw','imuoy',1)
# print(s1)
# # 再反转过来
# s1 = s1[::-1]
# print(s1)
#
# # 课外作业：我要替换指定第几个，怎么办？（字符串没有任何特点）

# 列表怎么拼成字符串
s = "will，roy，tufei，will，roy，will"
name = s.split('，')
print(name)
# join：把列表的元素，按分隔符拼成字符串
print('- '.join(name))
