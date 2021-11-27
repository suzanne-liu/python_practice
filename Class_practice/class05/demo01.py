# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 20:23
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：函数
"""


# 定义一个函数，my_replace是函数名字-用来调用函数，括号里面是函数的参数-运行时候传递进去
def my_replace(s, old='', new='', index=0):
    """
    替换出现在指定次数的字符串
    :param s: 源字符串
    :param old: 需要替换的字符串
    :param new: 新的替换字符串
    :param index: 替换的序号
    :return: 返回替换后的字符串
    """
    # 接下来你在这个缩进里面写的代码叫函数体
    # 前index个都替换为特殊字符串
    if not (old and index):
        # 代表函数执行完了，后面的代码不跑啦
        return s

    s = s.replace(old, '{replace}', index)
    # 再把前index-1个替换为旧的
    s = s.replace('{replace}', old, index - 1)
    # 把标识的字符串替换为新的字符串
    s = s.replace('{replace}', new)

    # 返回值，如果不写return，默认返回是None
    return s


# # 直接写在模块里面的代码（没有函数和类的封装），被导入的时候是会执行的
# # 函数默认是不执行的，必须调用才执行
# print('这是demo1')
# s = my_replace('abcdabcdabcdabcdabcd','ab','cd',1)
# print(s)


if __name__ == '__main__':
    # 把这个py文件作为运行文件的时候，才会执行这里的代码（测试代码都可以这样写）
    # 函数默认是不执行的，必须调用才执行
    print('这是demo1')
    s = input("请输入完整字符串：")
    a = input("请输入需要被替换的字符（串）：")
    b = input("请输入new字符（串）：")
    c =int(input("要替换第几个符合条件的字符（串）："))
    s = my_replace(s, a, b, c)
    print(s)
