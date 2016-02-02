# -*- coding: UTF-8 -*-

import string
import urllib2
import re

pattern=re.compile('<!--(.*?)-->',re.S)

content=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()


old_str=re.findall('<!--(.*?)-->',content,re.S)[0]
result=re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',old_str,re.S)

print "http://www.pythonchallenge.com/pc/def/%s.html" % "".join([c for c in result])

