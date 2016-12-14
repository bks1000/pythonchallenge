# encoding:utf8
#http://www.pythonchallenge.com/pc/def/channel.html

#http://www.pythonchallenge.com/pc/def/channel.zip 下载

import zipfile,re

z = zipfile.ZipFile('channel.zip','r')

#从readme.txt中获取的tip，开始的第一个文件
next="90052.txt"

comments = []
while True:
    
    #读取zip中的文件信息，此时拿到是数据是byte字节数组
    infomation=z.read(next)

    #将文件里的comment保存到list中
    comments.append(z.getinfo(next).comment)

    #因为re.findall需要对字符串数组做操作，所以将byte字节数组转换为字符串数组
    #除了下面这种转换方式，还有另外一种转换bytes.decode(infomation)  
    infomation=str(infomation)


    #根据正则表达式匹配文件中的数字内容，此时拿到的数据是list
    result=re.findall("[0-9]",infomation)

    #因为要获取数字，所以将匹配得到的list结果转换为string型。注意：用join方法的话，里面的参数需要保证所有元素都是string的list
    convert=''.join(result)

    #拼接下一个文件名
    next=convert+".txt"
    if next=='.txt':
        break

end=""
#因为comments是个字节List，因此需要对输出做处理（将List中的每个字节转化为字符串）
for list in comments:
    end+=str(list)

#输出comment
print (end)

#hockey X
#oxygen