# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 18:50:39 2022

@author: 박상일
"""

#%%
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

excel_file = openpyxl.Workbook()
excel_sheet1 = excel_file.active

excel_sheet1.title = '2022_07_08'

excel_sheet1.append(['순위','주식명','현재가','등락률'])
excel_sheet1.column_dimensions['A'].width = 20
excel_sheet1.column_dimensions['B'].width = 60
excel_sheet1.column_dimensions['C'].width = 20
excel_sheet1.column_dimensions['D'].width = 20

chromedriver = 'C:/Users/박상일/Python_basic_crawling/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get("https://finance.naver.com/sise/sise_quant.naver?sosok=0")

elems = driver.find_elements_by_css_selector("table tbody a")
prices = driver.find_elements_by_css_selector("#contentarea > div.box_type_l > table > tbody > tr > td:nth-child(3)")
climbs = driver.find_elements_by_css_selector("table tbody td:nth-child(5) span")
for index, elem, price, climb in zip(range(0,len(elems)), elems, prices, climbs):
    excel_sheet1.append([index+1, elem.text, price.text, climb.text])
    
excel_file.save('주식.xlsx')
excel_file.close()
time.sleep(1)
driver.quit()