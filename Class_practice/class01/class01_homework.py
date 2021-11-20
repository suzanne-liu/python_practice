# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 11:35 下午
@Function ：请输入模块功能描述
"""

"""题目一： 
设x=3,y=4
z满足(x的平方)+(y的三次方)
打印z的值

"""
x = int(input("请输入X值："))
y = int(input("请输入Y值："))
z = x ** 2 + y ** 3
print("z=" + str(z))


"""题目二：
你老婆对你说：“老公，晚上回来买一个西瓜，如果看到西红柿，就买两个西红柿。”
请用程序打印你从下班，到家的全过程

note:不要想那么多,就是题目字面意思
"""
a=input('下班了吗？yes or no：')
if a=='no':
    print("好吧，再见！")
else:
    print("太好了")
    b=input('有看到西瓜吗？yes or no:')
    if b=="yes":
        b1="一个西瓜"
        print("买一个西瓜带回来")
    else:
        print("买不到西瓜就算了")

    c = input('有看到西红柿吗？yes or no:')
    if c == "yes":
        c1="两个西红柿"
        print("买两个西红柿带回来")
    else:
        print("买不到西红柿就算了")
