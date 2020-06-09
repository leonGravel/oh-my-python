#!/usr/bin/python
# -*- coding: utf-8 -*-


import os, sys
path = raw_input('请输入文件路径(结尾加上/)：')   
#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)

n=0
for i in fileList:
    
    #设置旧文件名（就是路径+文件名）
    oldname=path + os.sep + fileList[n]   # os.sep添加系统分隔符
    
    #设置新文件名
    newname=path+ os.sep +fileList[n].replace('0529','0609')
    os.rename(oldname,newname)   #用os模块中的rename方法对文件改名
    process = str(oldname+'======>'+newname)
    print(process)
    
    n+=1