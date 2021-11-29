# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/27 12:47 下午
@Function ：冒泡排序
"""

from Class_practice.Sort import SrtingToList
import time

from Class_practice.class06.demo03_装饰器应用 import timer

@timer

def bubble_sort(ss):
    """
    冒泡排序的思路：
    1。从做往右俩俩比较，如果左边比右边大，就交换位置
    2。一轮之后就排出最大的数；
    3。相同方式进行第二轮，比较到倒数第二个，选出次大；
    4。进行len-1轮即可
    :param s:
    :return:
    """

    for i in range(1, len(ss)):
        print()
        print("--------第 " + str(i) + " 轮---------")
        for j in range(1, len(ss) - i + 1):
            if ss[j] < ss[j - 1]:
                ss[j], ss[j - 1] = ss[j - 1], ss[j]
            j += 1
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
        s= SrtingToList.StringToList(s)
    print("好的，本次要进行排序的数组为：" + str(s))
    t1=time.time()
    s = bubble_sort(s)
    t2=time.time()
    print()
    print("使用冒泡排序结果：" +str(s))
    print("所使用时间: "+str(t2-t1))
