#！usr/bin/env python
# -*- coding :  utf-8   -*-
import time
from urllib.request import urlopen
startTime=time.time()
data=urlopen("https://user.qzone.qq.com/1527447039/infocenter?")
data=data.read()
file=open("F:/1527.doc","wb")
file.write(data)
file.close()
endTime=time.time()
print(startTime-endTime)
