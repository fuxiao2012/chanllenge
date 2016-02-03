# -*- coding: UTF-8 -*-

import string
import urllib
import zipfile
import re


pattern=re.compile(r'(\d+)')
urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip', "channel.zip")
seed_str='90052.txt'
list=[]
with zipfile.ZipFile("channel.zip", "r") as f:
    while 1:
        res=pattern.findall(f.open(seed_str).read())
        if not res:
            break
        seed_str=res[0]+'.txt'
        list.append(f.getinfo(seed_str).comment)
        #print seed_str
    print f.open(seed_str).read()
    print "".join(list)

    
#print 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+seed_str
