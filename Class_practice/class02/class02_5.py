# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 10:30 下午
@Function ：循环
"""

# 1~100内，整数的和
# 分析1：1+2+3+……+100
"""
s = 0
s += 1
s += 2
……
s += 100
"""
# 循环初始数据
s = 0
i = 1
# 循环满足的条件
while i <= 100:
    s += i
    # 使用while语句的时候，需要自己控制每一次循环，循环控制变量的改变方式
    i = i + 1

print(s)

# FOR循环实现
"""
start: 循环从什么数值开始（次数的开始）（包含）
stop: 循环从什么数值结束（不包含）
step: 每循环1次，i增加多少（默认是1）
[start,stop) 左闭右开
"""
s = 0
for i in range(1,101):
    s += i

print(s)

w = 1
while w < 8:
    if w < 6:
        print('上班')
    else:
        print('玩')

    w += 1

for w in range(1,8):
    print("w的值："+str(w))
    if w < 6:
        print('上班')
    else:
        print('玩')

    # 这种写法是不生效的，因为每次循环开始都会使用上一次循环的w+step
    w += 2
    print("w+=2的值："+str(w))



# In的for循环
ss = 'abcde'
for s in ss:
    print(s)