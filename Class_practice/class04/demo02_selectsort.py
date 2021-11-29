# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/14 20:30
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：选择排序
"""

# python怎么交换两个变量的值
from Class_practice.class06.Decorator_time import sumtime

a = 1
b = 2
c = 3
a, b, c = c, b, a
print(a, b, c)

height = [166, 167, 155, 180, 177, 160, 178, 169, 155, 172]
# 身高从矮到高排

@sumtime()
def selects(height):
    # 重复这个操作，直到待排序元素只剩下一个
    for j in range(0,len(height)-1):

        # 每次从列表里面找出最大的放到最后
        # 记录找到的最大的下标
        max = 0
        for i in range(1, len(height)-j):
            # 当前遍历到的元素和最大的那个元素比
            if height[i] > height[max]:
                max = i

        # print(max)
        # 找出最大的后，我们把最大的和最后一个元素进行交换
        height[max], height[len(height) - 1 - j] = height[len(height) - 1 - j], height[max]

    print(height)

if __name__ == '__main__':
    selects(height)
