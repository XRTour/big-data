#！usr/bin/env python
# -*- coding :  utf-8   -*-


# 本课概要
# 1• 异常处理概述
# 2• 常见状态码及含义
# 3• URLError与HTTPError
# 4• 异常处理实战


# 1• 异常处理概述
# 异常处理概述
# 爬虫在运行的过程中，很多时候都会遇到这样或那样的异常。如果没有
# 异常处理，爬虫遇到异常时就会直接崩溃停止运行，下次再次运行时，
# 又会重头开始，所以，要开发一个具有顽强生命力的爬虫，必须要进行
# 异常处理。

# 常见状态码及含义
# 301 Moved Permanently：重定向到新的URL，永久性
# 302 Found：重定向到临时的URL，非永久性
# 304 Not Modified：请求的资源未更新
# 400 Bad Request：非法请求
# 401 Unauthorized：请求未经授权
# 403 Forbidden：禁止访问
# 404 Not Found：没有找到对应页面
# 500 Internal Server Error：服务器内部出现错误
# 501 Not Implemented：服务器不支持实现请求所需要的功能

# URLError与HTTPError
# 两者都是异常处理的类，HTTPError是URLError的子类，HTTPError有
# 异常状态码与异常原因，URLError没有异常状态码，所以，在处理的时
# 候，不能使用URLError直接代替HTTPError。如果要代替，必须要判断
# 是否有状态码属性。
# 接下来我们通过实战讲解。


#
# URLError：（产生的原因）
#
#     1.连不上服务器
#     2.远程的URL不存在
#     3.本地没有网络
#     4.触发了HTTPError子类


import urllib.error
import urllib.request
import re
try:
    req=urllib.request.urlopen("http://blog.csdn.net")
    reqd=req.read()
    pat='<li class=""><a href=".*">(.*?)</a></li>'
    data=re.compile(pat).findall(str(reqd))

    with open("F:/csdn1.txt","w+") as f:
        f.write(str(data))

except urllib.error.URLError as e:
    #判断URLError中是否有code（状态码）
    if hasattr(e,"code"):
        print(e.code)
    # 判断URLError中是否有reason
    if hasattr(e,"reason"):
        print(e.reason)
finally:
    print("OK...")


