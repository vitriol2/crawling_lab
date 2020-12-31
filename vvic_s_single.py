import selenium
from selenium import webdriver
import time
import bs4
import csv
from urllib.request import urlopen
import requests

# 시간초과시 에러를 발생시키고 넘어가기
import signal

from selenium.common.exceptions import TimeoutException


headers = {
    'authority': 'www.vvic.com',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.vvic.com/shop/59485',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,th;q=0.5',
    'cookie': '_ga=GA1.2.779926656.1608700034; hasCityMarket=""; cu=DB6681D1740A643FFC91ED23A49B6CB5; chash=516504396; _countlyIp=61.74.86.173; _uab_collina=160870025788701091732412; city=gz; ISSUPPORTPANGGE=true; _MYBID=%7B%22gz%22%3A%2212%22%7D; ipCity=121.162.16.212%2C%E9%A6%96%E5%B0%94%E7%89%B9%E5%88%AB%E5%B8%82%20%E9%A6%96%E5%B0%94%E7%89%B9%E5%88%AB%E5%B8%82; Hm_lvt_fdffeb50b7ea8a86ab0c9576372b2b8c=1608700258,1609133013,1609133038; Hm_lvt_fbb512d824c082a8ddae7951feb7e0e5=1608700258,1609133013,1609133038; hasFocusStall=false; mobile=; vvic_token=f19f12d7-0453-4bbc-becd-eaebcbfd2715; ut=0; uid=1795228; umc=0; pn=0; defaultShopId=; shopId=; uno=0; acw_tc=73eec0b116093164024502424ec7f4211054fdf62a8d5917e1f0738dcc; _gid=GA1.2.1103126014.1609316409; SSGUIDE=1; algo4Uid=132; algo4Cu=132; userLoginAuto=1; generateToken=eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJ2dmljLmNvbSIsInN1YiI6IjE3OTUyMjh8MjAyMDEyMzAxNjI5MDcwMjh8ZTgxMWYwNjkyNGYxNGVmODg5ZmMxM2M0ZTk4YzQ1ZjcifQ.cJ3aifchcDQJWNmmRAEB3tWlgBiYrm07hnIfdDS5fyJBxEkACpzFrfQcF16d1jXRrsO8KF6ij3P8M8_yz4kOgw; _gat=1; Hm_lpvt_fdffeb50b7ea8a86ab0c9576372b2b8c=1609317010; Hm_lpvt_fbb512d824c082a8ddae7951feb7e0e5=1609317010',
}


s = requests.Session()

url = 'https://www.vvic.com/gz/shops/12'
html = s.get(url, headers = headers).text
# html = urlopen(url).read()
soup = bs4.BeautifulSoup(html, 'html.parser')



floor_bulk = soup.find('div', class_="mk-shops mt10")
floor_list = floor_bulk.find_all('dl', 'stall-table clearfix')

floor_num = 5

shop_list_bulk = floor_list[floor_num].find('ul')
shop_list = shop_list_bulk.find_all('li')

# print(f'shop_list num: {len(shop_list)}')

shop_url = shop_list[4].find('a')['href']
html = s.get(f'https://www.vvic.com{shop_url}', headers = headers).text
bs = bs4.BeautifulSoup(html, 'html.parser')

# print(f'bs div num: {len(bs.find_all("div"))}')

body = bs.find('body')
shop_contact = body.find('div', class_='shop-info-con')
shop_contact_list = shop_contact.find_all('div', class_='contact-info')

print(f'shop_contact_list[1].text: {shop_contact_list[2].text}')
contact_full_text_list_length = len(list(str(shop_contact_list[1].text)))
contact_category = list(str(shop_contact_list[2].text))[:3]
contact_content = ''.join(list(str(shop_contact_list[2].text))[3:])
# contact_content = ''.join(list(str(shop_contact_list[3].text))[18:contact_full_text_list_length-13])
# contact_content_not_filtered = list(str(shop_contact_list[1].text))
# contact_content_letter_list = []
# for letter in contact_content_not_filtered:
#     if letter != '\n' & letter !='\t' & letter != '\r':
#         contact_content_letter_list.append(letter)
# contact_content = ''.join(contact_content_letter_list)
print(f'contact_category: {contact_category}')
print(f'contact_content: {contact_content}')


# shop_phone = shop_contact_list[1].text
# shop_wechat = shop_contact_list[2].text
# shop_qq = shop_contact_list[3].text
#
# # print(f'shop_contact_list: {shop_contact_list}')
#
# print(f'shop_contact_list: {shop_contact_list}')
#
# shop_info = []
# shop_phone = ''
# shop_wechat = ''
# shop_qq = ''
