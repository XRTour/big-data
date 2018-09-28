#！usr/bin/env python
# -*- coding :  utf-8   -*-

# 本课概要
# • 新闻爬虫需求及实现思路
# • 新闻爬虫编写实战
# • 作业


# 新闻爬虫需求及实现思路
# 需求：将新浪新闻首页（http://news.sina.com.cn/）所有新闻都爬到
# 本地。
# 思路：先爬首页，通过正则获取所有新闻链接，然后依次爬各新闻，并
# 存储到本地。


import urllib.request
import re
data=urllib.request.urlopen("https://news.sina.com.cn/").read()
#解码文件，如果出现错误，则ignore
data2=data.decode("utf-8","ignore")
pat='href="(https://news.sina.com.cn/.*?)">'
#数据清洗
allurl_prv=re.compile(pat).findall(data2)
print(allurl_prv)
pat2="(https://.*?.html)"
allurl=re.compile(pat2).findall(str(allurl_prv))
print(allurl)
try:
    for i  in  range(0,len(allurl)):

        """伪装浏览器"""
        # headers后面
        headers = ("user-agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
        # 添加一个报头信息
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        # 将oppner设为去全局
        urllib.request.install_opener(opener)

        """爬取"""
        print("第"+str(i)+"次爬取")
        this_url=allurl[i]
        file_path="F:/数据分析练习/news/"+str(i)+".html"
        thisurl_page=urllib.request.urlretrieve(this_url,file_path)
        print("----爬取成功-----")
except urllib.error.URLError as e:
    #判断URLError中是否有code（状态码）
    if hasattr(e,"code"):
        print(e.code)
    # 判断URLError中是否有reason
    if hasattr(e,"reason"):
        print(e.reason)


# 作业
# 爬取CSDN博客http://blog.csdn.net/首页显示的所有文章，每个文章
# 内容单独生成一个本地网页存到本地中。
# 难点：浏览器伪装、循环爬各文章
# 思路：先爬首页，然后通过正则筛选出所有文章url，然后通过循环分别
# 爬取这些url到本地。