# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 10:02 下午
@Function ：请输入模块功能描述
"""

"""
题目一：
x，y是整数，z = |x| + |y|
用编程实现，当x、y取不同值时，求z的值，打印出

分析：
x>=0,y>=0   z=x+y
x>=0,y<0   z=x-y
x<0,y>=0   z=-x+y
x<0,y<0   z=-x-y
"""
print("---------------题目一：x，y是整数，z = |x| + |y|   ;    用编程实现，当x、y取不同值时，求z的值，打印出------")
x = int(input("请输入x："))
y = int(input("请输入y："))
if x >= 0:
    if y >= 0:
        z = x + y
    else:
        z = x - y
else:
    if y >= 0:
        z = x + y
    else:
        z = -x - y
print("|x| + |y| = " + str(z))

"""
题目二：
求1-100内整数的和
题目分析：循环应该是1-100
"""
print("--------循环案例二：求1-100内整数的和-----------------")
s=0
for i in range(1,101):
   # print(i)
    s+=i
print("1-100内整数的和:"+str(s))

"""--------------将课程九九乘法表，以For循环实现 ==============="""
print('\n'*3)
print("------------题目：将课程九九乘法表，以For循环实现------------")

for i in range(1, 10):
    for j in range(1, 10):
        z = i * j
        if z < 10:
            print(str(j) + "X" + str(i) + "=" + str(z), end="  ")
        else:
            print(str(j) + "X" + str(i) + "=" + str(z), end=" ")
    print()

print('\n'*3)



print("------------题目：将课程九九乘法表，以While循环实现------------")
i1 = 1
j1 = 1
while i1 < 10:
    while j1 < 10:
        z = i1 * j1
        if z < 10:
            print(str(j1) + "X" + str(i1) + "=" + str(z), end="  ")
        else:
            print(str(j1) + "X" + str(i1) + "=" + str(z), end=" ")
        j1 += 1
    i1 += 1
    j1 = 1
    print()

print('\n' * 3)

print("------------0.6666666666  四舍五入保留两位小数---------")

s = 6 / 9
print(round(s, 2))

print("------------0.6666666666  截取留两位小数---------")

print(int(s * 10 ** 2) / (10 ** 2))

print('\n' * 3)
print("--------------用户名和密码都是字符串，长度为6-16位，如何判断一个用户名和密码长度是否合法？------------")

i = 0
while i == 0:
    username = input("请输入username:")
    if (len(username) < 6) or (len(username) >16):
        i = 0
        print("       > username的长度必须为6-16位，请重新输入!!!")
    else:
        i=1
        print("       > username的长度合法~~~")

i = 0
while i == 0:
    password = input("请输入password:")
    if (len(password) < 6) or (len(password) >16):
        i = 0
        print("       > password的长度必须为6-16位，请重新输入!!!")
    else:
        i=1
        print("       > password的长度合法~~~")

print('\n' * 3)

print("--------------九九乘法表只显示一半的三角形---------------")
for i in range(1, 10):
    for j in range(1, 10):
        z = i * j
        if j > i:
            break
        elif z < 10:
            print(str(j) + "X" + str(i) + "=" + str(z), end="  ")
        else:
            print(str(j) + "X" + str(i) + "=" + str(z), end=" ")
    print()

print('\n' * 3)
print("-------------九九乘法表去掉两条对角线---------------------")
for i in range(1, 10):
    for j in range(1, 10):
        z = i * j
        if i == j:
            print("      ", end="  ")
        elif i + j == 10:
            print("      ", end="  ")
        elif z < 10:
            print(str(j) + "X" + str(i) + "=" + str(z), end="  ")
        else:
            print(str(j) + "X" + str(i) + "=" + str(z), end=" ")
    print()

print('\n' * 3)
