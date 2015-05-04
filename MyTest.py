import os
import json

#读取指定目录下的文件
filePath=r'F:\TDDOWNLOAD\20'
if os.path.exists(filePath):
    print 'The file of this path exists.'
    size = os.path.getsize(filePath)
    if size != 0:
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
