#！usr/bin/env python
# -*- coding :  utf-8   -*-
#作用域
# i=0
#
# def func():
#     global j
#     j=10
#     j=j+1
# #     print(j)
# # print(str(j*100))
# # func()
# # print(str(j+j))
# # print(i)
# #形参和实参；
# def function(a,b):
#     if a>b:
#         print(a)
#     elif a==b:
#         print("=")
#     else:
#         print(b)
# function(6,6)

# import urllib
# from urllib.request import urlopen
# data1 = urlopen("http://www.baidu.com").read( )
# print(len(data1))
#
# data=urlopen("http://www.alipay.com").read()
# print(len(data))
from  urllib.request import urlopen
data=urlopen("http://www.baidu.com").read()
print(data)

