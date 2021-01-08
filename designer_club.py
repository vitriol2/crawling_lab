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

def delete_text_front_and_back(front_len, back_len, text):

    print(f'back_len: {back_len}')
    text_eng = ''.join(text[front_len:len(text)-back_len])
    print(f'text_eng: {text_eng}')
    return text_eng

def num_to_floor_name(num):
    if num<2:
        return f'B{num-2}'
    else:
        return f'F{num-1}'

def alarm_handler(signum, frame):
    print("Time is up!")
    raise TimeoutException

shop_info_list = []
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,th;q=0.5',
}

domain = 'http://designerclub.co.kr/floorguide'

s = requests.Session()
url = domain
html = s.get(url, headers = headers).text
soup = bs4.BeautifulSoup(html, 'html.parser')

paragraphs = soup.find_all('div', {'class': 'storeBox'})

floor_index = 0
for paragraph in paragraphs:
    shop_info_list = []
    li_shop_list = paragraph.find('ul').find_all('li')
    print(f'floor_index: {floor_index}')
    for li_shop in li_shop_list:

        shop_info = []
        desc = li_shop.find('div', {'class': 'desc'})

        # 매장 번호, 영어이름, 한굴이름
        span_name = desc.find('span', {'class': 'name'})
        a_shop_number_name = desc.find('a')
        shop_num = ''.join(a_shop_number_name.find_all('strong')[0].text.split(' '))
        print(f'shop_num: {shop_num}')
        print(f'shop_num_len: {len(shop_num)}')
        shop_name = a_shop_number_name.find_all('strong')[1].text
        print(f'shop_name: {shop_name}')
        print(f'shop_name: {len(shop_name)}')
        shop_name_eng_mixed = a_shop_number_name.text

        print(f'shop_name_eng_mixed: {shop_name_eng_mixed}')
        print(f'shop_name_eng_mixed_len: {len(shop_name_eng_mixed)}')
        shop_name_eng = delete_text_front_and_back(len(shop_num), len(shop_name),shop_name_eng_mixed)

        # print(f'shop_name_eng: {shop_name_eng}')

        # 매장 전화번호
        span_tel = desc.find('span', {'class': 'tel'})
        i_tel = span_tel.find('i')
        shop_tel = span_tel.text

        shop_info.append(shop_num)
        shop_info.append(shop_name)
        shop_info.append(shop_name_eng)
        shop_info.append(shop_tel)

        shop_info_list.append(shop_info)


    floor_name = num_to_floor_name(floor_index)
    f = open(f'designer_club/designer_club_shopList_floor_{floor_name}.csv', 'w', encoding='utf-8', newline='')
    csvWriter = csv.writer(f)
    for i in shop_info_list:
        # i[0] = i[0].decode('utf-8')
        csvWriter.writerow(i)

    f.close()

    floor_index += 1
    # print(f'shop_info_list: {shop_info_list}')
# print(f'shop_info_list: {shop_info_list}')