# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 22:03
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：快速排序
"""
import time

from Class_practice.class06.demo03_装饰器应用 import timer

height = [166, 167, 155, 180, 177, 160, 178, 169, 155, 172] * 300

@timer()
def quick_sort(height, left=0, right=len(height) - 1):
    """
    快速排序
    :param height: 待排序列表
    :param left: 递归排的时候，下标开始位置
    :param right: 递归排的时候，下标结束位置
    :return:
    """
    # 选取最右边的为基准
    base = height[right]

    # l,h交换的指针
    l, h = left, right

    while l < h:
        # 第一步
        while l < h:
            # 从左往右找比基准大的，交换到h位置， h往左移动一位；
            if height[l] <= base:
                l += 1
            else:
                height[l], height[h] = height[h], height[l]
                h -= 1
                # 如果找到了，循环就终止了
                break

        # 第二步
        while l < h:
            # 再从h位置从右往左找比基准小的，交换到之前l的位置，l往右移动一位。
            if height[h] >= base:
                h -= 1
            else:
                height[l], height[h] = height[h], height[l]
                l += 1
                # 如果找到了，循环就终止了
                break

    if l<=left:
        # 左出口
        pass
    else:
        # 递归左边
        quick_sort(height,left, l - 1)

    if h>=right:
        # 右出口
        pass
    else:
        # 递归右边
        quick_sort(height,h + 1, right)



t1 = time.time()
quick_sort(height)
# print(height)
t2 = time.time()
print(t2-t1)