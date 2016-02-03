# -*- coding: UTF-8 -*-

import string
import urllib2
import pickle
import pprint

pkl_file=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
data1 = pickle.load(pkl_file)
print 
for i in data1:
    print "".join([j[0]*int(j[1]) for j in i])
    
#pprint.pprint(data1)

