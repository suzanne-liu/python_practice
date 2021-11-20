# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 10:18 下午
@Function ：逻辑运算：对bool值进行运算，实质是多个比较的最终结果
"""
# 如满足x大于0 且 x是整数，那么我们把这种数叫自然数
# x = int(input('请输入一个数：'))
# if type(x) == int and x > 0:
#     print('是自然数')
# else:
#     print('不是自然数')

# not：非
print(not False)

# and：与（而且）
print(True and True)

# or：或（或者）
print(True or False)

# 优先级：not > and > or
"""
短路原则：
    and短路：False and True and False（只要and之前的结果为False，那么后面的就不执行）
        表达式只有and
    or短路：True or False or True
        如果表达式里面既有and，又有or，最终生效的一定是or的短路

    好处：
        可以提升程序运行效率

    要求（复杂点的表达式一定要用括号来明确表示你的优先级和运行顺序）
"""
# 运行原理（短路原则决定逻辑运算符前后表达式是否运行）
# True or True and b
print(True or not False and b)

# 运行原理（短路生效是在逻辑运算符左边按优先级计算出来后，才考虑短路）
# False or (True and a)
#print(False and True or True and a)



print("----------'输入'练习-------------")
z=input("你的名字叫什么，请输入：")
print("哦，你叫 "+z)