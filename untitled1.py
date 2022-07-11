# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 14:46:16 2022

@author: 박상일
"""

#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#드라이버 생성
chromedriver = 'C:/Users/박상일/Python_basic_crawling/chromedriver'
driver = webdriver.Chrome(chromedriver)

#크롤링할 사이트 호출
driver.get('https://davelee-fun.github.io/')
elems = driver.find_elements_by_css_selector("section.recent-posts div.card-body > h4")
for data in elems:
    print(data.text)    #원하는 데이터 추출

#멀티 페이지 크롤링
for item in range(5): #5페이지 크롤링
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") #윈도우 창을 설정한 전체 높이로 이동
    last = driver.find_elements_by_css_selector(".ml-1.mr-1") #리스트 형식의 data추출
    last[-1].click()
    
    time.sleep(2)
    
    elems = driver.find_elements_by_css_selector("section.recent-posts div.card-body > h4")
    for data in elems:
        print(data.text)    #원하는 데이터 추출

driver.quit()