# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/14 21:20
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：杨辉三角
"""
# 深拷贝与浅拷贝
mylist1 = [1, 2, 3]
# # 浅拷贝：只拷贝了指针
# mylist2 = mylist1
# mylist2[1] = 22
# print(mylist1)
#
# # 深拷贝：拷贝了内存里面的值
# mylist1 = [1,2,3]
# # mylist2 = mylist1[0:]
# mylist2 = mylist1.copy()
# mylist2[1] = 22
# print(mylist1)


# # 先把n次方系数推算出来
# n = int(input("请输入杨辉三角的次方数："))
# mylen = int(input("指定每个数字输出多少位（偶数）："))
#
# # 0次方就只有1个系数1
# arr1 = [1]
#
# # 打印等腰三角形（格式化输出）
# # 先输出 mylen * yh / 2 个空格
# print()
# print("%*s" % (int(mylen * n / 2), ''), end='')
# for d in arr1:
#     print('%-*d' % (mylen,d))
#
# arr2 = [1]
#
# for j in range(1, n + 1):
#     # 下一次推导，需要把arr1变成arr2里面的元素
#     arr1 = arr2.copy()
#
#     # 下一个次方，要多一系数
#     arr2.append(0)
#
#     for i in range(len(arr2)):
#         # 开始和末尾两个都是1
#         if i == 0 or i == len(arr2) - 1:
#             arr2[i] = 1
#         else:
#             # 如果不是开始和末尾，那么它等于肩膀上两个数的和
#             arr2[i] = arr1[i - 1] + arr1[i]
#
#     print("%*s" % (int(mylen * (n-j) / 2), ''), end='')
#     # 在同一行输出列表所有元素
#     for d in arr2:
#         print('%-*d' % (mylen, d),end='')
#     # 输出完成后换行
#     print()
