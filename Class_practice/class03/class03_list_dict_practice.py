# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/11 21:56
@Auth ： Mr. William 1052949192
@Company ：特斯汀学院 @testingedu.com.cn
@Function ：列表和字典的应用
"""
import json

# 抓包获取ip接口的返回值
res = 'jQuery110208559019740755636_1636639051842({"Srcid":"5809","ResultCode":"0","status":"0","QueryID":"3351941526","Result":[{"DisplayData":{"strategy":{"tempName":"ip","precharge":"0","ctplOrPhp":"1"},"resultData":{"tplData":{"srcid":"5809","resourceid":"5809","OriginQuery":"113.218.173.100","origipquery":"113.218.173.100","query":"113.218.173.100","origip":"113.218.173.100","location":"\u6e56\u5357\u7701\u957f\u6c99\u5e02\u5cb3\u9e93\u533a \u7535\u4fe1","userip":"","showlamp":"1","tplt":"ip","titlecont":"IP\u5730\u5740\u67e5\u8be2","realurl":"http:\/\/www.ip138.com\/","showLikeShare":"1","shareImage":"1","data_source":"AE"},"extData":{"tplt":"ip","resourceid":"5809","OriginQuery":"113.218.173.100"}}},"ResultURL":"http:\/\/www.ip138.com\/","Weight":"2","Sort":"1","SrcID":"5809","ClickNeed":"0","SubResult":[],"SubResNum":"0","ar_passthrough":[],"RecoverCacheTime":"0"}],"data":[{"srcid":"5809","resourceid":"5809","OriginQuery":"113.218.173.100","origipquery":"113.218.173.100","query":"113.218.173.100","origip":"113.218.173.100","location":"\u6e56\u5357\u7701\u957f\u6c99\u5e02\u5cb3\u9e93\u533a \u7535\u4fe1","userip":"","showlamp":"1","tplt":"ip","titlecont":"IP\u5730\u5740\u67e5\u8be2","realurl":"http:\/\/www.ip138.com\/","showLikeShare":"1","shareImage":"1"}],"ResultNum":"1"})'

# 需求1：把结果变成标准格式的json字符串
# 从左往右找到{位置
# 从右往左找到}的位置
res = res[res.find('{'):res.rfind('}')+1]
print(res)

# s = '["1",2,3,4,]'
# print(s)

# 转为字典
# 快捷导入：选中库名，按Alt+Enter，选择导入
res = json.loads(res)
print(res)

