#！usr/bin/env python
# -*- coding :  utf-8   -*-


# 本课概要
# • 课前说明
# • 作业讲解
# • 关于学习方法
# • urllib基础
# • 超时设置
# • 自动模拟HTTP请求

# 1.
# urllib基础
# 要系统学习urllib模块，我们从urllib基础开始。这个知识点中，我们会
# 为大家实战讲解urlretrieve()、urlcleanup()、info()、getcode()、
# geturl()等


# urlretrieve() 爬取网页并且将其放在本地对应的地方
"""
from urllib.request import urlretrieve,urlcleanup
URL="http://www.taobao.com"
LOCAL_HOST_PATH="F:/数据分析练习/taobao1.html"
rts=urlretrieve(URL,LOCAL_HOST_PATH)
urlcleanup()
# urlcleanup()清理掉urlretrieve()的缓存
"""

#info(）展现环境信息
"""
from urllib import request
data = request.urlopen("http://www.Tmall.com")
print(data.info())
//
Server: Tengine
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Connection: close
Vary: Accept-Encoding
Date: Thu, 27 Sep 2018 10:53:56 GMT
Vary: Accept-Encoding
Vary: Origin, Ali-Detector-Type
x-server-id: wormholesource011008070003.na61
realpath: page/portal/act/fp
Cache-Control: max-age=0, s-maxage=120
ETag: W/"37e61-/BCqUMEYH8E6gTGQ93NCfi2+aCE"
x-readtime: 696
x-via: cn764.l1, cache9.cn764, l2cn241.l2, cache17.l2cn241, wormholesource011008070003.na61
EagleEye-TraceId: 7cc8715815380456354415595e
Strict-Transport-Security: max-age=0
Timing-Allow-Origin: *, *
Via: cache17.l2cn241[0,200-0,H], cache8.l2cn241[1,0], cache7.cn548[0,200-0,H], cache7.cn548[1,0]
Age: 97
Ali-Swift-Global-Savetime: 1530790205
X-Cache: HIT TCP_MEM_HIT dirn:-2:-2
X-Swift-SaveTime: Thu, 27 Sep 2018 10:53:58 GMT
X-Swift-CacheTime: 118
EagleId: dbee144715380457339058245e
Strict-Transport-Security: max-age=31536000
//

"""

# 3.  getcode()获取状态码
"""
from urllib import request
data = request.urlopen("http://www.Tmall.com")
print(data.getcode())
#200
"""

# 4.  geturl() 获取目标网址
"""
from urllib import request
data = request.urlopen("http://www.Tmall.com")
print(data.geturl())
# https://www.tmall.com/
"""


# 超时设置
# 由于网络速度或对方服务器的问题，我们爬取一个网页的时候，都需要
# 时间。我们访问一个网页，如果该网页长时间未响应，那么我们的系统
# 就会判断该网页超时了，即无法打开该网页。
# 有的时候，我们需要根据自己的需要，来设置超时的时间值，比如，有
# 些网站反应快，我们希望2秒钟没有反应，则判断为超时，那么此时，
# timeout的值就是2，再比如，有些网站服务器反应慢，那么此时，我
# 们希望100秒没有反应，才判断为超时，那么此时timeout的值就是
# 100。接下来为大家实战讲解爬取时的超时设置。
"""
from urllib import request
URL="https://www.baidu.com"
data = request.urlopen(URL, timeout=5)
# data=data.decode("utf-8")
print(data.getcode(), data.geturl(), str(data.read(), "utf-8"))

from urllib import request
for i  in range(0,100):
    try:
        file=request.urlopen("https://www.baidu.com",timeout=5)
        data = file.read()
        print(len(data),end="")
    except Exception  as er:
        print("出现异常"+er,end="")
    finally:
        print("第"+str(i+1)+"次---------------")
"""

# 自动模拟HTTP请求
# 客户端如果要与服务器端进行通信，需要通过http请求进行，http请求
# 有很多种，我们在此会讲post与get两种请求方式。比如登陆、搜索某
# 些信息的时候会用到。
# 接下来我们通过实战讲解。


#get请求    www.baidu.com?ie=utf-8
"""
from urllib import request
keywd="肖军"
#quote()解决中文编码问题
keywd=request.quote(keywd)
url="http://www.baidu.com/s?wd="+keywd+"&ie=utf-8&tn96542061_hao_pg"
#  http不要加s，因为此处没有证书
# 获取一个request请求request.Request(),封装成一个HTTP请求，
req=request.Request(url)
#用urlopen()打开一个一个HTTP请求
reqw=request.urlopen(req).read()
file=open("F:/数据分析练习/肖军_baidu.txt","wb")
file.write(reqw)
file.close()
"""

#post请求
import urllib.request
import urllib.parse
url="https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F"
#设置表单form信息(关注name属性对应的值就行）
mydata=urllib.parse.urlencode(
    {"loginname":"1101@qq.com",
     "password":"110110110"}
    ).encode("utf-8")
#封装成为一个post请求
req=urllib.request.Request(url,mydata)
#伪装成为一个浏览器
# req.add_header()
#获取post请求
reqw=urllib.request.urlopen(req).read()
file=open("F:\数据分析练习/jd.txt","wb")
file.write(reqw)
file.close()

