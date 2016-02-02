# -*- coding: UTF-8 -*-

import string
import urllib2
import re

pattern=re.compile('<!--(.*?)-->',re.S)

content=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()


#for m in re.findall('<!--(.*?)-->',content,re.S):
#    print m

old_str=re.findall('<!--(.*?)-->',content,re.S)[1]

print "http://www.pythonchallenge.com/pc/def/%s.html" % "".join([c for c in old_str if c in string.letters])

