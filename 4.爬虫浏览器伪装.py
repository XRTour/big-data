#！usr/bin/env python
# -*- coding :  utf-8   -*-
# 本课概要
# • 浏览器伪装技术原理
# • 浏览器伪装技术实战

# 浏览器伪装技术原理：在 header中加入user-agent伪装成为浏览器
# 我们可以试试爬取csdn博客，我们发现会返回403，因为对方服务器会
# 对爬虫进行屏蔽。此时，我们需要伪装成浏览器才能爬取。
# 浏览器伪装我们一般通过报头进行，接下来我们通过实战分析一下

# 浏览器伪装技术实战
# 由于urlopen()对于一些HTTP的高级功能不支持，所以，我们如果要修
# 改报头，可以使用urllib.request.build_opener()进行，当然，也可以
# 使用urllib.request.Request()下的add_header()实现浏览器的模拟。
# 我们重点讲前者方法，后者方法是否掌握无所谓，有兴趣并有时间的同
# 学可以自行研究第2种方法，接下来通过实战讲解

import urllib.request
url="https://blog.csdn.net"
#headers后面
headers=("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
#添加一个报头信息
opener=urllib.request.build_opener()
opener.addheaders =[headers]
#将oppner设为去全局
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
print(data)
file=open("F:/伪装浏览器.html","w+")
file.write(str(data))
file.close()

import urllib.request
url="https://blog.csdn.net"
#headers后面
headers=("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
#添加一个报头信息
opener=urllib.request.build_opener()
opener.addheaders =[headers]
data=opener.open(url).read()
print(data)
file=open("F:/伪装浏览器oppner.html","w+")
file.write(str(data))
file.close()


# #导入urllib.request模块
# import urllib.request
# url="https://blog.csdn.net"
# #设置请求头
# headers=("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
# #创建一个opener
# opener=urllib.request.build_opener()
# #将headers添加到opener中
# opener.addheaders=[headers]
# #将opener安装为全局
# urllib.request.install_opener(opener)
# #用urlopen打开网页
# data=urllib.request.urlopen(url).read().decode('gbk','ignore')
# print(data)
#
# file=open("F:/liulanqi.html","w+")
# file.write(str(data))
# file.close()


