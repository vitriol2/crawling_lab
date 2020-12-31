import selenium
from selenium import webdriver
import time
import bs4
import csv
from urllib.request import urlopen


# url = f'https://www.vvic.com/gz/shops/12'
# html = urlopen(url).read()
# soup = bs4(html, 'html.parser')
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By

chromedriver_dir = r'/Users/apple/Documents/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver_dir)

driver.get('https://www.vvic.com/gz/shops/12')

shop_info_list = []


floors_bulk = driver.find_element(By.CLASS_NAME, 'mk-shops.mt10')
floor_list = floors_bulk.find_elements(By.CLASS_NAME,'stall-table.clearfix')
# print(len(floor_list))
floor_num = 5

shop_list_bulk = floor_list[floor_num].find_element(By.TAG_NAME, 'ul')
shop_list = shop_list_bulk.find_elements(By.TAG_NAME, 'li')

print(f'shop_list[0]: {shop_list[0].find_element(By.TAG_NAME, "a").get_attribute("href")}')

shop_list[0].click()
#
# # 샵 목록
# # shop_num = 1
# shop_info = []
# # shop = shop_list[shop_num]
#
#
# shop_num = 0
# for shop in shop_list:
#     print(f'shop_num: {shop_num}')
#     shop_name = shop.find_element(By.TAG_NAME, 'div').text
#     shop_info.append(shop_name)
#
#     try:
#
#         # 샵 상세로 들어가기
#         driver.find_element(By.XPATH, f"/html/body/div[6]/div[3]/div[2]/dl[1]/dd/ul/li[{shop_num + 1}]/a").click()
#
#         tabs = driver.window_handles
#
#         driver.switch_to.window(tabs[-1])
#         # driver.switch_to(tabs[-1])
#
#         # 샵 정보 보기
#         try:
#             source = driver.page_source
#             bs = bs4.BeautifulSoup(source, 'html.parser')
#
#             body = bs.find('body')
#             div_list = body.find('div', class_='w clearfix shop-wrap')
#             shop_content = div_list.find('div', class_='shop-content shop-content-top')
#             mt10 = shop_content.find('ul', class_='mt10')
#             shop_contact_list = mt10.find_all('li')
#
#             shop_phone = shop_contact_list[3].text
#             shop_wechat = shop_contact_list[4].text
#             shop_qq = shop_contact_list[5].text
#
#             shop_info.append(shop_phone)
#             shop_info.append(shop_wechat)
#             shop_info.append(shop_qq)
#
#             shop_info_list.append(shop_info)
#
#             shop_num += 1
#         except AttributeError:
#             source = driver.page_source
#             bs = bs4.BeautifulSoup(source, 'html.parser')
#
#             shop_contact = bs.find('div', class_='shop-info-con')
#             shop_contact_list = shop_contact.find_all('div', class_='contact-info')
#
#             shop_phone = shop_contact_list[1].text
#             shop_wechat = shop_contact_list[2].text
#             shop_qq = shop_contact_list[3].text
#
#             shop_info.append(shop_phone)
#             shop_info.append(shop_wechat)
#             shop_info.append(shop_qq)
#             shop_info.append('s')
#
#             shop_info_list.append(shop_info)
#
#             shop_num += 1
#         except NoSuchElementException:
#             source = driver.page_source
#             bs = bs4.BeautifulSoup(source, 'html.parser')
#
#             shop_contact = bs.find('div', class_='shop-info-con')
#             shop_contact_list = shop_contact.find_all('div', class_='contact-info')
#
#             shop_phone = shop_contact_list[1].text
#             shop_wechat = shop_contact_list[2].text
#             shop_qq = shop_contact_list[3].text
#
#             shop_info.append(shop_phone)
#             shop_info.append(shop_wechat)
#             shop_info.append(shop_qq)
#             shop_info.append('s')
#
#             shop_info_list.append(shop_info)
#
#             shop_num += 1
#
#         driver.close()
#         driver.switch_to.window(tabs[0])
#
#     except selenium.common.exceptions.ElementClickInterceptedException:
#         print(f'intercepted shop_num: {shop_num}')
#         shop_num += 1
#
#     except selenium.common.exceptions.InvalidSessionIdException:
#         print(f'InvalidSessionIdException shop_num: {shop_num}')
#
#         shop_num += 1
#     # 샵 목록으로 돌아오기
#     # print(f'show_info: {shop_info}')
#
#
# print(f'shop_info_list: {shop_info_list}')