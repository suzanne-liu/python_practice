# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/28 12:29 上午
@Function ：回文字符串
"""

"""
判断是否是回文串思路：
设定左右两个指针left,right
[0,1,2,3,4,5]
1。如果是偶数长度，从两头开始判断，需要判断到left=(len(s)/2)-1 包含关系
[0,1,2,3,4,5，6]
2。如果是奇数长度，从两头开始判断，需要判断到left=（(len(s)-1）/2)-1 包含关系
"""

s="ieieieie"

def IfPalindrome(s):
    left = 0
    right = len(s) - 1
    if len(s) % 2 == 0:  # 偶数长度，
        middle = len(s) / 2  # 终止判断
    else:
        middle = (len(s) - 1) / 2

    while left < middle:
        if s[left] != s[right]:
            print("不是回文串")
            return False
        else:
            left += 1
            right -= 1
    if left == middle:
        print("是回文串")
        return True

IfPalindrome(s)