import selenium
from selenium import webdriver
import time
import bs4
import csv
from urllib.request import urlopen
import requests


# 시간초과시 에러를 발생시키고 넘어가기
import signal


from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By

def num_to_floor_name(num):
    if num<2:
        return f'B{num-2}'
    else:
        return f'F{num-1}'

def alarm_handler(signum, frame):
    print("Time is up!")
    raise TimeoutException

shop_info_list = []

domain = 'http://www.theot.org/htm/theot_info02.htm'

chromedriver_dir = r'/Users/apple/Documents/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver_dir)

driver.get(domain)

# 일일히 하나하나 찾아서 find하지말고
# xpath를 통해 한번에 원하는 부분을 찾을 수 있다.
floor_button_group = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[5]/td/table/tbody/tr')
tr_list = floor_button_group.find_elements_by_tag_name('td')
print(len(tr_list))

floor_index = 0
for tr_floor in tr_list:
    print(f'tr_floor: {tr_floor}')
    tr_floor.click()

    time.sleep(1)

    # tag이름을 통해 iframe부분을 찾는다.
    iframe = driver.find_element_by_tag_name('iframe')

    # 사이트 전체에 초점이 맞춰져 있는 driver를
    # iframe부분으로 selenium의 driver를 위치시켜야 한다.
    driver.switch_to.frame(0)

    html = driver.page_source

    soup = bs4.BeautifulSoup(html, 'html.parser')

    tbody = soup.find('tbody')
    tr_list2 = tbody.find_all('tr')
    print(f'tr_list length: {len(tr_list2)}')

    shop_info_list = []

    # 내가 찾던 리스트의 index=0부분은 칼럼명이어서 제외시켰다.
    #
    for tr in tr_list2[1:]:
        shop_info = []
        td = tr.find_all('td')
        # print(f'td[0].text: {td[2].text}')
        shop_info.append(td[0].text)
        shop_info.append(td[2].text)
        shop_info.append(td[3].text)
        shop_info.append(td[4].text)

        shop_info_list.append(shop_info)

    #
    floor_name = num_to_floor_name(floor_index)
    f = open(f'{floor_name}.csv', 'w', encoding='utf-8', newline='')
    csvWriter = csv.writer(f)
    for i in shop_info_list:
        # i[0] = i[0].decode('utf-8')
        csvWriter.writerow(i)

    f.close()


    driver.switch_to.window(driver.window_handles[-1])

    #안정적인 클릭 전환을 위해 시간차를 두었다.
    time.sleep(2)

    floor_index += 1


# print(tbody_inner)

#
# driver.get(domain)
#
# iframe = driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame(0)
#
#
#
# html = driver.page_source
