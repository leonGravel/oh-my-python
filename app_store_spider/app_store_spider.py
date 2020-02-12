# 给女朋友写的脚本，导出appstore里面竞品的评价

import urllib.request
import json
import xlsxwriter
print("这是一个在线获取appstore里任意app的评论列表工具")
print("运行完毕后 将生成一个名为“app评论.xlsx”的文件")
page=1;
appid=input("请输入应用id号:");
#appid=1182886088
workbook = xlsxwriter.Workbook('app评论.xlsx')
worksheet = workbook.add_worksheet()
format=workbook.add_format()
format.set_border(1)
format.set_border(1)
format_title = workbook.add_format()    
format_title.set_border(1)   
format_title.set_bg_color('#cccccc')
format_title.set_align('left')
format_title.set_bold()    
title=['昵称','标题','评分','评论内容']
worksheet.write_row('A1',title,format_title)
row=1
col=0
count=0

#默认循环10次  
while page<11:
    myurl="https://itunes.apple.com/rss/customerreviews/page="+str(page)+"/id="+str(appid)+"/sortby=mostrecent/json?l=en&&cc=cn"
    response = urllib.request.urlopen(myurl)
    myjson = json.loads(response.read().decode())
    print("正在生成数据文件，请稍后......"+str(page*10)+"%")
    if "entry" in myjson["feed"]:
        count+=len(myjson["feed"]["entry"])
        #循环写入第1列：昵称
        for i in myjson["feed"]["entry"]:
            worksheet.write(row,col,i["author"]["name"]["label"],format)
            row+=1
        #循环写入第2列：标题    
        row=1+(page-1)*50
        for i in myjson["feed"]["entry"]:
            worksheet.write(row,col+1,i["title"]["label"],format)
            row+=1
        # 循环写入第3列: 评分
        row=1+(page-1)*50
        for i in myjson["feed"]["entry"]:
            worksheet.write(row,col+2,i["im:rating"]["label"],format)
            row+=1
        #循环写入第3列：内容
        row=1+(page-1)*50
        for i in myjson["feed"]["entry"]:
            worksheet.write(row,col+3,i["content"]["label"],format)
            row+=1
        page=page+1
        row=(page-1)*50+1
    else:
        print("正在生成数据文件，请稍后......100%")
        break
if count==0:
    print("运行完毕，未获取到任何数据。请检查是否输入正确！")
else:
    print("生成完毕，请查阅相关文件,共获取到"+str(count)+"条数据")
workbook.close()