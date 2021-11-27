# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/27 1:31 下午
@Function ：字符串转数组
"""

def StringToList(s):
    if str(type(s))!= "<class 'str'>":
        print(str(s)+" not a string, please double check.")
    else:
        # s2=s.split(",")
        s2 =s.replace("[","")
        s2 = s2.replace("]", "")
        s2=s2.split(",")
    print(s2)
    return s2

if __name__ == '__main__':
    s="[1,7,2,4,5]"
    StringToList(s)
