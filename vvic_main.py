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


def addShop(shops, num):
    try:
        print(f'addShop num: {num}')
        shop = shops[num]
        shop_info = []
        shop_name = shop.find_element_by_tag_name('div').text
        shop_info.append(shop_name)

        # shop.click()
        driver.execute_script("arguments[0].click()", shop)
        # 샵 정보 담기
        tabs = driver.window_handles

        driver.switch_to.window(tabs[-1])

        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'html.parser')
        # entire = bs.find('ul', class_='quickSearchResultBoxSidoGugun')
        # li_list = bs.find('div', class_='shop-info-con')

        # print(li_list)

        shop_contact = bs.find('div', class_='shop-info-con')
        shop_contact_list = shop_contact.find_all('div', class_='contact-info')

        shop_phone = shop_contact_list[1].text
        shop_wechat = shop_contact_list[2].text
        shop_qq = shop_contact_list[3].text

        shop_info.append(shop_phone)
        shop_info.append(shop_wechat)
        shop_info.append(shop_qq)

        shop_info_list.append(shop_info)

        driver.close()
        driver.switch_to.window(tabs[0])

        time.sleep(1)
    except AttributeError:
        print(f'AttributeError: {num}')

        tabs = driver.window_handles

        driver.close()
        driver.switch_to.window(tabs[0])
    except TimeoutException:

        print(f'TimeoutException: {num}')

        tabs = driver.window_handles

    # print(shop_info_list)
    except ElementClickInterceptedException:
        print(f'ElementClickInterceptedException: {num}')


    except NoSuchElementException:
        # print('NoSuchElementException: ' + num)
        print(f'NoSuchElementException: {num}')



chromedriver_dir = r'/Users/apple/Documents/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver_dir)

driver.get('https://www.vvic.com/gz/shops/12')

shop_info_list = []

# time.sleep(5)
# floor = driver.find_element_by_class_name('stall-tabel.clearfix')
floor = driver.find_element_by_class_name('floor-item.clearfix')
# loca.click()

# 샵 이름 담기
shops = floor.find_elements_by_tag_name('a')

# 중간에 안되는 카페시점부터 다시 출력하기 위해서
num = 0
for shop in shops:
    try:
        if num == len(shops)-1:
            break
        addShop(shops, num)
        num += 1
    except AttributeError:
        print(f'AttributeError: {num}')

        tabs = driver.window_handles

        driver.close()
        driver.switch_to.window(tabs[0])
        num += 1
    except TimeoutException:

        print(f'TimeoutException: {num}')

        tabs = driver.window_handles

        num += 1
# print(shop_info_list)
    except ElementClickInterceptedException:
        print(f'ElementClickInterceptedException: {num}')

        addShop(shop, num)
        num += 1

    except selenium.common.exceptions.NoSuchElementException:
        # print('NoSuchElementException: ' + num)
        print(f'NoSuchElementException: {num}')
        addShop(shop, num)
        num += 1

f = open(f'shopList2.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in shop_info_list:
    csvWriter.writerow(i)

f.close()

#
# for i in shop:
#     # print(shop.text)
#     shop_info.append()
#     shop.click()
