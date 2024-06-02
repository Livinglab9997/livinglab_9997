# - 240419 ~ 240519를 기준으로 조회된 모든 페이지 크롤링

from selenium.webdriver.common.keys import Keys
import time
import requests
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =====================================================================================================
### TEST 
# num = 1
# url = f"https://www.animal.go.kr/front/awtis/roadCat/roadCatList.do?totalCount=8762&pageSize=12&menuNo=5000000025&&page={num}"

# # 창 열기
# driver = webdriver.Chrome()
# driver.get(url)

# bs = BeautifulSoup(driver.page_source, 'html.parser')

# # result = bs.find_all('div', 'date')
# result = bs.find_all('li','subject')

# for re in result:
#     title = re.get_text(strip=True) # 타이틀
#     print(title)
    
#     print('-'*50)

# time.sleep(1)
# driver.quit()

# =====================================================================================================
### TEST 
# 창 열기
# driver = webdriver.Chrome()
# driver.get(url)

# bs = BeautifulSoup(driver.page_source, 'html.parser')

# result = bs.find_all('li', 'info')

# for re in result:
#     text = re.find_all('div','value')
#     for t in text:
#         print(t.get_text(strip=True))
#     print('-'*25)

# time.sleep(1)
# driver.quit()

# =====================================================================================================
### selenium 사용 버전 (동적이라 느림 ;;)
action = False
if action :
    for num in range(1, 735):
        url = f"https://www.animal.go.kr/front/awtis/roadCat/roadCatList.do?totalCount=8762&pageSize=12&menuNo=5000000025&&page={num}"
        # 창 열기
        driver = webdriver.Chrome()
        driver.get(url)
        bs = BeautifulSoup(driver.page_source, 'html.parser')
        total_list = []
        result = bs.find_all('li')
        # result = bs.find_all('li', 'info')
        for rst in result:
            sample = []
            # info = rst.find_all('li', 'info')
            info = rst.find_all('div', 'value')
            if len(info) > 0 :
                for i in info:
                    text = i.get_text(strip=True)
                    sample.append(text)
            subject = rst.find_all('li', 'subject')
            if len(subject) > 0 :
                for s in subject:
                    text = s.get_text(strip = True)
                    sample.append(text)
            if (len(sample) > 0) : 
                total_list.append(sample)
        time.sleep(1)
        driver.quit()
        print(num, end = ' ')
        if num % 20 == 0 : print()

# =====================================================================================================
import requests
from bs4 import BeautifulSoup
import time

total_list = []
for num in range(1, 735):
    url = f"https://www.animal.go.kr/front/awtis/roadCat/roadCatList.do?totalCount=8762&pageSize=12&menuNo=5000000025&&page={num}"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    result = bs.find_all('li')
    for rst in result:
        sample = []
        info = rst.find_all('div', 'value')
        if len(info) > 0:
            for i in info:
                text = i.get_text(strip=True)
                sample.append(text)
        subject = rst.find_all('li', 'subject')
        if len(subject) > 0:
            for s in subject:
                text = s.get_text(strip=True)
                sample.append(text)
        if len(sample) > 0:
            total_list.append(sample)
    time.sleep(1)
    print(num, end=' ')
    if num % 20 == 0:
        print()
# 결과 확인 (원하는 대로 total_list를 출력하거나 저장할 수 있습니다)
print(total_list)