import urllib2
import urllib
import re
import os
import sys

url = 'http://amoredware/feka.cr?uid=746c44803dbd1dc3c929630387ea148c'
a='http://armoredware'
b=''
c='uid=746c44803dbd1dc3c929630387ea148cc12223'
urlOld = url

x = 0

while x < 31000:

	request = urllib2.Request(url)
	request.add_header('Referer', urlOld)

	response = urllib2.urlopen(request)
	data = response.read()
	f= open("numoflinks.txt","a+")
	f.write('%s,%s\n'%(x,url))

	try:
		
		scan = re.search('AAA-.*.-\d\d\d\d',data)
		flag = scan.group(0)
		if flag is not None:
			print(flag)

	except Exception as e:
		pass
		

	m = re.search('\/orders\/.*.?\?',data)
	b = m.group(0)


	urlOld = url

	url = a + b + c
	#print("Scanning: ",url)
	
	x = x + 1
	#print(webContent[0:300])
