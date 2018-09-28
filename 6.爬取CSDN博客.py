#！usr/bin/env python
# -*- coding :  utf-8   -*-
# 作业
# 爬取CSDN博客http://blog.csdn.net/首页显示的所有文章，每个文章
# 内容单独生成一个本地网页存到本地中。
# 难点：浏览器伪装、循环爬各文章
# 思路：先爬首页，然后通过正则筛选出所有文章url，然后通过循环分别
# 爬取这些url到本地。

import urllib.request
import re

#伪装成为浏览器
url="https://blog.csdn.net"
#headers后面用元组添加 user-agent
headers=("user-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
#添加一个报头信息
opener=urllib.request.build_opener()
opener.addheaders =[headers]
data=opener.open(url).read()
data2=data.decode("utf-8","ignore")

#对爬取页面的

# 信息进行清洗
pat='href="(https://blog.csdn.net/.*)"\starget="_blank"'
data2_str=str(data2)
allurl=re.compile(pat).findall(data2_str)
print(allurl)

#遍历文章链接列表
try:
    for i in range(0,len(allurl)):
        print("第"+str(i+1)+"次爬取",end="")
        this_url=allurl[i]
        file_path="F:/数据分析练习/csdn_eassy/"+str(i+1)+".html"
        this_url_html=urllib.request.urlretrieve(this_url,file_path)
        print("----------ok--------")
except urllib.request.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
finally:
    print("一共爬取"+str(i)+"个文件")
