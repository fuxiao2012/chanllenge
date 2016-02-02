# -*- coding: UTF-8 -*-

import string

old_str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr \
ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
frm="".join(map(chr, range(ord('a'), ord('z')+1)))
to=frm[2:]+frm[0:2]
#print frm
#print to
trans=string.maketrans(frm,to)
new_str=string.translate(old_str, trans)

print new_str

old_url="http://www.pythonchallenge.com/pc/def/map.html"
print "http://www.pythonchallenge.com/pc/def/%s.html" % string.translate("map", trans)
