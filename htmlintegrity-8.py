# encoding:utf-8
#http://www.pythonchallenge.com/pc/def/integrity.html
#资料 http://www.w3school.com.cn/tags/att_img_usemap.asp
'''<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->'''
#和压缩解压缩有关,BZh91AY&SY这是代表一种bzip2的压缩算法的.应该使用bz2模块
import bz2

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

username = bz2.decompress(un)
password = bz2.decompress(pw)
print (username,password)

#('huge', 'file')
#
#import bz2
#
#print bz2.compress('NiNiuBi')
#print bz2.decompress('BZh91AY&SY\x96\xb1\x1a|\x00\x00\x00\x85\x80\x10\x01\x00 \x02\x00 \x00!\x8c\x834\xd1`\xc3\x8b\xb9"\x9c(HKX\x8d>\x00')
#print bz2.decompress('BZh91AY&SY("UZ\x00\x00lP\x00k\xd8H\x00 \x00t\x12 \x8d4\x10\xa9=A\x93g\tY \x08e\x05\xcd\nFiM\xa4\xe2T\xc9\x99UB\x81\xb6\x87\x0c\n\x15\xef\xb2\x17\x11\xd0\xd4^\x12\x91\x8d\x89\xb2\x00!k=\xde|]\xc9\x14\xe1B@\xa0\x89Uh')