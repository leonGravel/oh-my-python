# 给女朋友写的脚本，导出http://drugs.dxy.cn/以及https://www.mvyxws.com的疾病数据

import requests
from bs4 import BeautifulSoup
import xlsxwriter 

def request_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def save_to_excel_dxy(soup):
    workbook = xlsxwriter.Workbook('药理分类汇总.xlsx')
    sheet = workbook.add_worksheet()
    sheet.set_column('A:A', 20)
    sheet.set_column('B:B', 30)

    sheet.write('A1', '药理分类')
    sheet.write('B1', '药品类型')
    n = 1
    list = soup.select('li[name = cur_cate]')
    for item in list:
        drugs_category = item.find('a').get_text()
        drugs_attr_onclick = item.find('a').attrs['onclick']
        
        s = drugs_attr_onclick.find(',')
        e = drugs_attr_onclick.find(')')
        drugs_type = drugs_attr_onclick[s+1:e]
        item_id = 'cate_'+drugs_type
        item_list = soup.find(id=item_id).find_all('h3')
        

        for durgs_item in item_list:
            sheet.write(n, 0, drugs_category)
            sheet.write(n, 1, durgs_item.find('a').get_text())

            n = n + 1
    workbook.close()    


def save_to_excel_mvyxws(soup):
    workbook = xlsxwriter.Workbook('疾病分类汇总.xlsx')
    sheet = workbook.add_worksheet()
    sheet.set_column('A:A', 20)
    sheet.set_column('B:B', 30)
    sheet.write(0, 0, '疾病分类')
    sheet.write(0, 1, '疾病名称')
    n = 1
    list = soup.find_all('section')[1].select('.category')

    for item in list:
        item_category = item.find('h2').get_text()
        item_category = item_category[1:len(item_category)]
        
        item_list = item.find('p').find_all('a')
        for durgs_item in item_list:
           
            sheet.write(n, 0, item_category)
            sheet.write(n, 1, durgs_item.get_text())
            n = n + 1
    workbook.close()    


def get_dxy():
    url = 'http://drugs.dxy.cn/'
    html = request_page(url)
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel_dxy(soup)

def get_mvyxws():
    url = 'https://www.mvyxws.com'
    html = request_page(url)
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel_mvyxws(soup)
 
if __name__ == '__main__':
    get_dxy()
    get_mvyxws()
