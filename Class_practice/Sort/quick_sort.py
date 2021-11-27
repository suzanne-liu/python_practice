# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/27 2:37 下午
@Function ：快速排序
"""
"""
快速排序思路：选取最后一个元素为基准，把元素分成左右两部分，左边都比基准小，右边都比基准大
1。从左往右找比基准大的，交换到right位置， right往左移动一位 (right=right--)；现在base在left。
2。现在base在left， 再从right 位置从右往左找比基准小的，交换到之前base（left）的位置，left往右移动一位（left=left++)。现在base在right。
3。反复执行前面的操作，直到left=right，因为这个时候说明整个列表的元素都和基准进行了比较。也就达到了基准前面的元素都比基准小，基准后面的元素都比基准大。
4。当整个递归执行到列表只有一个元素的时候，就可以保证整个列表是有序的。
"""

from Class_practice.Sort import SrtingToList
import time

ss = [166, 167, 155, 180, 177, 160, 178, 169, 155, 172]


def quick_sort(ss, start=0, end=len(ss) - 1):
    """

    :param ss: 要排序的数组
    :param start: 数组起始下标
    :param end: 数组结束下标
    """
    # 设置本轮基准
    base = end
    left = start
    right = end
    while left < right:  # 执行完while表示已经执行完一轮，这时候left=right
        # 从左往右走
        while left < right:
            if ss[left] > ss[base]:
                ss[left], ss[base] = ss[base], ss[left]  # 这时候base值在left位置上
                base = left  # 这步容易忘，别忘了
                right -= 1  # 为下一次比较做准备，right位置已经是刚才比较过去的值了，所以往左移一位
                break
            else:
                left += 1  # 表示left位置上的并不比base大，继续下一位

        # 从右往左走
        while left < right:
            if ss[right] < ss[base]:
                ss[right], ss[base] = ss[base], ss[right]  # 这时候base值在right位置上
                base = right  # 这步容易忘，别忘了
                left += 1  # 为下一次比较做准备，left位置已经是刚才比较过去的值了，所以往右移一位
                break
            else:
                right -= 1  # 表示right位置上的并不比base小，继续下一位

    # 递归操作
    #     如果 right+1<end 就要排序右边 否则 不做操作  如果 left-1>start 就要排序左边，否则不做操作。
    if left > start:
        quick_sort(ss, start, left - 1)
    # 递归退出条件：其实就是left-1<=start的时候啥也不做
    if right < end:
        quick_sort(ss, right + 1, end)
    return ss


if __name__ == '__main__':
    print("默认数组是：[166, 167, 155, 180, 177, 160, 178, 169, 155, 172]")
    tihuan = input("你要替换这个数组吗？要替换请输入yes: ")
    if tihuan != "yes":
        print("您选择的是不替换")
    else:
        ss = input("请输入数字型数组：")
        ss = SrtingToList.StringToList(ss)
    print("好的，本次要进行排序的数组为：" + str(ss))
    t1=time.time()
    s = quick_sort(ss)
    t2 = time.time()
    print()
    print("使用快速排序结果：" + str(ss))
    print("所使用时间： "+str(t2-t1))
