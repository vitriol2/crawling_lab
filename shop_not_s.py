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

#
# chromedriver_dir = r'/Users/apple/Documents/crawling/chromedriver'
# driver = webdriver.Chrome(chromedriver_dir)
#
# driver.get('https://www.vvic.com/gz/shops/12')
#
# shop_info_list = []
#
# floors_bulk = driver.find_element_by_class_name('mk-shops.mt10')
# floor_list = floors_bulk.find_elements_by_class_name('stall-table.clearfix')
# # print(len(floor_list))
# floor_num = 0
#
# shop_list_bulk = floor_list[floor_num].find_element_by_tag_name('ul')
# shop_list = shop_list_bulk.find_elements_by_tag_name('li')
#
# # print(len(shop_list))
# shop = shop_list[1]
#
# shop_info = []
# shop_name = shop.find_element_by_tag_name('div').text
# shop_info.append(shop_name)
#
# # shop.click()
# driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[2]/dl[1]/dd/ul/li[2]/a").click()
# # driver.find_element_by_xpath(f"/html/body/div[6]/div[3]/div[2]/dl[1]/dd/ul/li{2}/a").click()
#
# tabs = driver.window_handles
#
# driver.switch_to.window(tabs[-1])

# source = driver.page_source

# search = input('검색어를 입력하세요. : ')



chromedriver_dir = r'/Users/apple/Documents/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver_dir)

driver.get('https://www.vvic.com/shop/14963')

try:
    splash = driver.find_element_by_class_name("stall-focus-guide.shop-upstyle-guide.introjs-showElement");
    splash_btn = splash.find_element_by_xpath('/html/body/div[9]/a').click()
except AttributeError:
    print('no splash')

# url = driver.page_source
# soup = bs4.BeautifulSoup(url, 'html.parser')

# print(soup)

shop_overall = driver.find_element_by_class_name('body_shop3.gz')
shop_factor_list = shop_overall.find_element_by_xpath('/html/body/div[8]/div[2]/div')
shop_contact_list_group = shop_factor_list.find_element_by_tag_name('ul')
shop_contact_list = shop_contact_list_group.find_elements_by_tag_name('li')

shop_phone = shop_contact_list[3].find_element_by_class_name('text').text
shop_wechat = shop_contact_list[4].find_element_by_class_name('text').text
shop_qq = shop_contact_list[5].find_element_by_class_name('text').text
# shop_contact = shop_overall.find_elements_by_tag_name('div')

print(f'shop_contact: {shop_qq}')