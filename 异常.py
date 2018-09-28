#！usr/bin/env python
# -*- coding :  utf-8   -*-
def func():
    print("my")
    prnt("Ki")
try:
    func()
except Exception as er :
    print(er,end="")
    print("======="+"这就是异常")
finally:
    print("dabaojian")