# encoding:utf8

#http://www.pythonchallenge.com/pc/def/oxygen.html
# Description: get usefull message from png picture, using Image module

import  urllib
from PIL import Image
'''
#下载图片
imgurl = 'http://www.pythonchallenge.com/pc/def/oxygen.png'

f = open('oxygen.png','wb')
f.write(urllib.urlopen(imgurl).read())
f.close()
'''


image = Image.open('F:\\HW\\pythonchallenge\\pythonchallenge\\oxygen.png')  
data = image.convert('L').getdata()  #http://www.2cto.com/kf/201603/492898.html
     
message = []  
for i in range(3,608,7):  
    message.append(chr(data[image.size[0]*50+i]))  
print ''.join(message)  

nextLvl = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join([chr(i) for i in nextLvl])


#integrity