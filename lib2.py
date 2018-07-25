import urllib2
import urllib
import re
import os
import sys

url = 'http://armoredware/lub.bf?uid=746c44803dbd1dc3c929630387ea148c'
a='http://armoredware'
b=''
c='uid=746c44803dbd1dc3c929630387ea148c12344'
urlOld = 'http://armoredware/orders/molif.se?uid=746c44803dbd1dc3c929630387ea148c'

x = 0

while x < 31000:

	request = urllib2.Request(url)
	request.add_header('Referer', urlOld)

	response = urllib2.urlopen(request)
	data = response.read()
	f= open("lib_url.txt","a+")
	f.write('%s\n'%(url))

	m = re.search('\/orders\/.*.?\?',data)
	b = m.group(0)
	urlOld = url

	url = a + b + c
	print("Scanning: ",url)
	
	x = x + 1
	#print(webContent[0:300])
