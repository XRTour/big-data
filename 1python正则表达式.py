#！usr/bin/env python
# -*- coding :  utf-8   -*-


# 原子
# a普通字符作为原子abcd.....
# b非打印字符作为原子 \n \t  \d   \w  \s
# c通用字符作为原子[jsx]、
# d原子表
# 接下来进行实战讲解


# 1.  普通字符作为原子
import re
pat="yue"
string="http://yum.iqianyue.com"
ew=re.findall(pat,string)
print(str(ew))
print("\t")
print(str(ew))
#2.非打印字符作为原子
# \n 换行符
# \t 下一个制表符
# \d  一个十进制数
# \w 任意一个字母数字下划线
#  \s  匹配空白的字符
#  \S \D  与小写互补

import re

pat="\w\dpython\w"
string="op1pythonpop12pythonpsdddddddddddddddddddddddddp12pythonpsd"
tr=re.findall(pat,string)
print(tr)

pat="pytho[now]n"
string="pythonnioioipiipythowniiiuiu"
tr=re.findall(pat,string)
print(tr)


# 元子符
# 所谓的元字符，就是正则表达式中具有一些特殊含义的字符，比如重复
# N次前面的字符等。
#
#     *  0,1,1+
#     ?  0,1次
#     +  1，1+
#     .  匹配除(\n)之外任意字符
#     ^  匹配开始
#     $  匹配结束
#     {n } 前面的原子字符出现n次
#      {,n},{m,},{m,n}
#      | 模式选择符，表示或的意思
import re
pat="python..."
string="pythonopoppythonxiaojunpythonSDF"
tr=re.findall(pat,string)
print(tr)


#模式修正符：

# 所谓的模式修正符，即可以在不改变正则表达式的情况下，通过模式修
# 正符改变正则表达式的含义，从而实现一些匹配结果的调整等功能。

#  I  不区分大小写
#  M  多行匹配
#  L  本地化识别匹配
#  U  根据Unicode字符，解析字符
#  S  让(.)匹配换行符（\n)
import  re
pat1="python"
pat2="python"
string="hiuhdwiidwiuheiPython"
tt=re.findall(pat2,string,re.I)
print(tt)

# 贪婪模式* 与懒惰模式?  +
# 贪婪模式的核心点就是尽可能多的匹配，
# 而懒惰模式的核心点就是尽可能少的匹配。


#正则表达式函数
# 正则表达式函数有
# re.match()函数  ：重头开始匹配,头如果不匹配，立马end。
# re.search()函数 ：从左至右，搜索一个满足条件的
# 全局匹配函数 re.compile(pat1).findall(string)  ：pat1:正则表达式
# re.sub()函数,


import re
pat="p.*y"
string='''puguwgugeuugecgwucguecguyypuguwgugeuugecgw
       ucguecguyypuguwgugeuugecgwucwwwguecguyyvvpuguwgugeuugecgwucguecguyyvpuguwgugeuugecgwucguecguyyvvpuguwgugeuugecgwucguecguyyv'''
data=re.compile(pat).findall(string)
print(data)


# 接下来为大家讲解如何匹配.com或.cn网址，以及如何匹配电话号码。
pat="[a-zA-Z]+://[^\s]*[.com|.cn]"
string="<a href='https://www.baidu.com'>sjiij</a>"  #用单引号区别网址
rts=re.findall(pat,string)
print(rts)

#匹配电话号码
pat="\d{3}\s\d{4}\s\d{4}"
string = "123 4568 4578,145 126 8977 8978,125 6365 5689 ,148 1259 4569,152 1456 589"
rts = re.findall(pat,string)
print(rts)


#简单的爬虫简单的爬虫很好写，直接使用urllib即可编写，接下来我们为大家讲解如何爬取csdn。

# from urllib.request import urlopen
# pat="<div.*>.*</div>"
# data=urlopen("https://read.douban.com").read()
# rts=re.compile(pat).findall(str(data))
# gh = open("F:/xiaju______n.doc","w")
# gh.write(str(rts))
# gh.close()

#采集douban的出版社

from urllib.request import urlopen
pat = '<div class="name">(.*?)</div>'
URL="https://read.douban.com/provider/all"
data=urlopen(URL).read()
data=data.decode("utf-8")
data_rts=re.compile(pat).findall(data)
#写入txt文本文件
file=open("F:/rows_Lines_n.txt","w")
fo for row in data_rts:

    file.write(str(row)+"\n")
file.close()






