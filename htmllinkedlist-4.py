#http://www.pythonchallenge.com/pc/def/linkedlist.php
#http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

import urllib2
import time
import random

uri = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
data = '12345'

send_headers = {
 'Host':'www.pythonchallenge.com',
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
 'Connection':'keep-alive',
 'Cache-Control': 'no-cache',
 'Pragma': 'no-cache',
 'Accept-Language': 'zh-CN,zh;q=0.8',
 'Cookie':'info=you+should+have+followed+busynothing...',
 'Upgrade-Insecure-Requests': '1'
}

count = 0
olddata = ''

while True:
    try:
        req = urllib2.Request(uri+data,headers=send_headers)
        src = urllib2.urlopen(req,timeout=60)
        html = src.read()
        olddata = data
        data = html.split(' ')[-1]
        print '%d---%s\r\n' % (count,data)
        src.close()
        if count==399:
            print 'result:%s' % data
            break
        count = count+1
        time.sleep(3)
    except Exception:
        data = olddata
    
    
#peak.html
#http://www.pythonchallenge.com/pc/def/peak.html
    
