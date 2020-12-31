import selenium
from selenium import webdriver
import time
import bs4
import csv
from urllib.request import urlopen

# 시간초과시 에러를 발생시키고 넘어가기
import signal


# url = f'https://www.vvic.com/gz/shops/12'
# html = urlopen(url).read()
# soup = bs4(html, 'html.parser')
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By

def alarm_handler(signum, frame):
    print("Time is up!")
    raise TimeoutException

# chromedriver_dir = r'/Users/apple/Documents/crawling/chromedriver'
# driver = webdriver.Chrome(chromedriver_dir)
# # driver.delete_all_cookies()
#
# driver.get('https://www.vvic.com/gz/shops/12')
#
# shop_info_list = []
#
#
# floors_bulk = driver.find_element(By.CLASS_NAME, 'mk-shops.mt10')
# floor_list = floors_bulk.find_elements(By.CLASS_NAME,'stall-table.clearfix')
# print(len(floor_list))


url = f'https://www.vvic.com/gz/shops/12'
html = urlopen(url).read()
soup = bs4.BeautifulSoup(html, 'html.parser')

floor_bulk = soup.find('div', class_="mk-shops mt10")
floor_list = floor_bulk.find_all('dl', 'stall-table clearfix')
print(len(floor_list))


shop_list_bulk = floor_list[1].find('ul')
shop_list = shop_list_bulk.find_all('li')

print(f'shop_list num: {len(shop_list)}')

