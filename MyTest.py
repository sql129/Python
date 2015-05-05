import urllib2
import os
import json

#指定网址文件下载到本地
url = 'http://quote.gf.com.cn/kline/daily/sz/000776/20'
f = urllib2.urlopen(url) 
data = f.read()
filepath = 'F:\\TDDOWNLOAD\\20'
with open(filepath,'w') as code:
    code.write(data)

#读取指定目录下的文件
filePath=r'F:\TDDOWNLOAD/20'
if os.path.exists(filePath):
    print 'The file of this path exists.'
    size = os.path.getsize(filePath)
    if size != 0:
        print 'The file is not empty.'
        file_object = open(filePath)
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()


#每组数据的CHECK
        locations=json.loads(all_the_text)    
        i = 0
    
        for location in locations:
            i=i+1
            high = location["high"]
            low  = location["low"]
            avg  = location["avg"]
        
            if avg >= low and avg <= high:
                result = 'The '+str(i)+ ' data is OK.'
                print result
            else:
                result = 'The '+str(i)+ ' data is NG.'
                print result
    else:
        print 'The byte of this file is ZERO.'
else:
    print 'The file of this path is NG.'
