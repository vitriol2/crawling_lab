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

def addShopNotS(shop, num, shop_info):



    print(f'addShopNotS num: {num}')
    # 샵 정보 담기

    # try:
    #     splash = driver.find_element_by_class_name("stall-focus-guide.shop-upstyle-guide.introjs-showElement");
    #     splash_btn = splash.find_element_by_xpath('/html/body/div[9]/a').click()
    # except :
    #     print('no splash')

    driver.execute_script("arguments[0].click()", shop)
    # 샵 정보 담기
    tabs = driver.window_handles

    driver.switch_to.window(tabs[-1])

    shop_overall = driver.find_element_by_tag_name('body_shop3.gz')
    shop_factor_list = shop_overall.find_element_by_xpath('/html/body/div[8]/div[2]/div')
    shop_contact_list_group = shop_factor_list.find_element_by_tag_name('ul')
    shop_contact_list = shop_contact_list_group.find_elements_by_tag_name('li')

    shop_phone = shop_contact_list[3].find_element_by_class_name('text').text
    shop_wechat = shop_contact_list[4].find_element_by_class_name('text').text
    shop_qq = shop_contact_list[5].find_element_by_class_name('text').text

    shop_info.append(shop_phone)
    shop_info.append(shop_wechat)
    shop_info.append(shop_qq)

    shop_info_list.append(shop_info)

    driver.close()
    driver.switch_to.window(tabs[0])


def addShop(shop, num, shop_info):
    # try:

        print(f'addShop num: {num}')
        # shop = shops[num]
        # 샵 정보 담기

        # shop_overall = driver.find_element_by_tag_name('body')

        # shop_overall = driver.find_element_by_class_name('body_shop3.gz')
        # shop_factor_list = shop_overall.find_element_by_id('content_slzz_home')
        # div_list = shop_overall.find_elements_by_tag_name('div')
        # print(f'shop_factor_list: {shop_factor_list}')

        # source = driver.page_source
        # soup = bs4.BeautifulSoup(source, 'html.parser')
        # content_slzz_home = soup.find('div', id_='content_slzz_home')
        # print(f'content_slzz_home: {content_slzz_home}')

        # shop_contact_list = shop_factor_list.find_element_by_class_name('contact-info')
        #
        # shop_phone = shop_contact_list[1].find_element_by_class_name('text').text
        # shop_wechat = shop_contact_list[2].find_element_by_class_name('text').text
        # shop_qq = shop_contact_list[3].find_element_by_class_name('text').text
        #
        #
        # shop_info.append(shop_phone)
        # shop_info.append(shop_wechat)
        # shop_info.append(shop_qq)
        # shop_info.append('s')
        # shop_name = shop.find_element_by_tag_name('div').text
        # shop_info.append(shop_name)
        #
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

        # time.sleep(1)

    # except AttributeError:
    #     print(f'AttributeError: {num}')
    #     # num += 1
    # except ElementClickInterceptedException:
    #     print(f'ElementClickInterceptedException: {num}')


    # except selenium.common.exceptions.NoSuchElementException:
    #     # print('NoSuchElementException: ' + num)
    #     print(f'NoSuchElementException: {num}')



chromedriver_dir = r'/Users/apple/Documents/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver_dir)

driver.get('https://www.vvic.com/gz/shops/12')

shop_info_list = []

floors_bulk = driver.find_element_by_class_name('mk-shops.mt10')
floor_list = floors_bulk.find_elements_by_class_name('stall-table.clearfix')
# print(len(floor_list))
floor_num = 0

shop_list_bulk = floor_list[floor_num].find_element_by_tag_name('ul')
shop_list = shop_list_bulk.find_elements_by_tag_name('li')

# print(len(shop_list))

num = 0
for shop in shop_list:
    if num == len(shop_list):
        break
    shop = shop_list[num]
    tabs = driver.window_handles

    driver.find_element_by_xpath(f"/html/body/div[6]/div[3]/div[2]/dl[1]/dd/ul/li[{num + 1}]/a").click()
    driver.switch_to.window(tabs[-1])
    shop_info = []
    try:
        # if num == len(shop_list)-1:

        shop_name = shop.find_element_by_tag_name('div').text
        shop_info.append(shop_name)

        # shop.click()

        addShopNotS(shop, num, shop_info)
        num += 1
    except AttributeError:
        print(f'AttributeError: {num}')

        num += 1
    except TimeoutException:

        print(f'TimeoutException: {num}')
# print(shop_info_list)
    except ElementClickInterceptedException:
        print(f'ElementClickInterceptedException: {num}')
        num += 1

    except selenium.common.exceptions.NoSuchElementException:
        # print('NoSuchElementException: ' + num)
        print(f'NoSuchElementException: {num}')
        addShop(shop, num, shop_info)

        num += 1


f = open(f'shopList_floor_1.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in shop_info_list:
    csvWriter.writerow(i)

f.close()



