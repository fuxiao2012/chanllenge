# -*- coding: UTF-8 -*-

import string
import urllib
import zipfile
from PIL import Image 
import re

pattern=re.compile(r'(\d+)')

urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/oxygen.png', "oxygen.png")
im=Image.open("oxygen.png")
print(im.format, im.size, im.mode)
rst="".join([chr(im.getpixel((i, 50))[0]) for i in range(2, 629,7) ])
print rst
print len(rst)
print "http://www.pythonchallenge.com/pc/def/%s.html" % "".join([chr(int(str)) for str in pattern.findall(rst)])
 



