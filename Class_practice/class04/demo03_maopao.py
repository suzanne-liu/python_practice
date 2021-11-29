# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/14 20:47
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：冒泡排序
"""
#import time
from Class_practice.class06.demo03_装饰器应用 import timer

height = [166, 167, 155, 180, 177, 160, 178, 169, 155, 172] * 300

@timer()
def maop(height):
    #t1 = time.time()
    for j in range(len(height) - 2):
        # 每一轮冒出最大的来
        # 最多交换len(height) -1 次
        for i in range(1, len(height) - j):
            # 前一个比后一个大，就交换（冒泡）
            if height[i] < height[i - 1]:
                height[i], height[i - 1] = height[i - 1], height[i]

    return height

# print(height)
# print(height)
#t2 = time.time()
#print(t2-t1)

if __name__ == '__main__':
    maop(height)