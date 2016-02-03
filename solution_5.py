# -*- coding: UTF-8 -*-

import string
import urllib2
import re

pattern=re.compile(r'(\d+)')
content=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php').read()
seed_str=re.search(r'<a href="linkedlist.php\?nothing=(\d+)">', content).group(1)
seed_url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+seed_str
content=urllib2.urlopen(seed_url).read()
#print content
while 1:
    m=pattern.search(content)
    if not m:
        break;
    print seed_str
    seed_str= m.group(0)   
    content=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+seed_str).read()
#process Divide by two
seed_url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(int(seed_str)/2)
content=urllib2.urlopen(seed_url).read()
while 1:
    m=pattern.findall(content)
    if not m:
        break;
    #for text with more than one number    
    seed_str= m[len(m)-1]  
    print seed_str 
    content=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+seed_str).read()
    
print 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+seed_str
