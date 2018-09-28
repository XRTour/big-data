#！usr/bin/env python
# -*- coding :  utf-8   -*-
#99乘法口诀
for i  in range(1,10):
    for j in range(1,i+1):
        # print(i,"*",j,"=",i*j,"   " ,end="" )
        print(str(i)+"*"+str(j)+"="+str(i*j)," ",end="")
    print("\n")

##倒着排出
for i in range(9,0,-1):
    for j in range(i,0,-1):
        print(str(i)+"*"+str(j)+"="+str(i*j)," ",end="")
    print("\n")