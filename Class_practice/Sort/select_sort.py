# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/27 1:24 下午
@Function ：选择排序
"""
import time

from Class_practice.Sort import SrtingToList


def select_sort(ss):
    """
    选择排序的思路：
    1。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
    2。再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    3。重复第二步，直到所有元素均排序完毕。

    本次例子，进行升序排列，找最小值
    :param s:
    :return:
    """

    for i in range(0, len(ss)):
        print()
        print("--------第 " + str(i) + " 轮---------")
        minIndex=i    #初始化，先假定第i位是最小值
        for j in range(i+1, len(ss)):
            if ss[j]<ss[minIndex]:
                minIndex=j
            j += 1
        ss[i],ss[minIndex]=ss[minIndex],ss[i]
        i += 1
        print(ss)
    return ss


if __name__ == '__main__':
    s = [166, 167, 155, 180, 177, 160, 178, 169, 155, 172]
    print("默认数组是：[166, 167, 155, 180, 177, 160, 178, 169, 155, 172]")
    tihuan = input("你要替换这个数组吗？要替换请输入yes: ")
    if tihuan != "yes":
        print("您选择的是不替换")
    else:
        s = input("请输入数字型数组：")
        s = SrtingToList.StringToList(s)
    print("好的，本次要进行排序的数组为：" + str(s))
    t1=time.time()
    s = select_sort(s)
    t2=time.time()
    print()
    print("使用选择排序结果：" + str(s))
    print("所使用时间： "+str(t2-t1))

