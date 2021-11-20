# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 10:26 下午
@Function ：分支语句
"""
 #示例z = |x + 3| + |y|
"""分析：
    x + 3 >=0 而且 y >= 0的时候：z = x + 3 + y
    x + 3 <0 而且 y >= 0的时候：z = -(x + 3) + y
    x + 3 >=0 而且 y < 0的时候：z = x + 3 - y
    x + 3 <0 而且 y < 0的时候：z = -(x + 3) - y
"""
x = int(input('请输入x的值：'))
y = int(input('请输入y的值：'))


print("这里有if  elif  else 的用法")
if (x + 3 >= 0) and (y >= 0):
    z = x + 3 + y
elif x + 3 < 0 and y >= 0:
    z = -(x + 3) + y
elif x + 3 >= 0 and y < 0:
    z = x + 3 - y
else:
    z = -(x + 3) - y

print(z)

if x + 3 >= 0:
    if y >= 0:
        z = x + 3 + y
    else:
        z = x + 3 - y
else:
    if y >= 0:
        z = -x - 3 + y
    else:
        z = -x - 3 - y

print(z)
