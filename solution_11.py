# -*- coding: UTF-8 -*-

#add a line for test git
#add a ssh test
import string
import re

a = ['1', '11', '21', '1211', '111221']
for i in xrange(5, 31):
    nums=a[i-1]
    init=nums[0]
    cnt=1
    rst=''
    for j in nums[1:]:
        if j == init:
            cnt+=1
            continue
        rst+=str(cnt)+init
        init=j
        cnt=1    
    rst+=str(cnt)+init    
    a.append(rst)
    #print "%d:%s " % (i, a[i])
print len(a[30])    
