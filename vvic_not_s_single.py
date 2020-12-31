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
def text_split(content):
    # print(f'content: {content}')
    text = str(content)
    text_list = list(text)
    text_length = len(text_list)
    # print(f'text: {text}')
    letter_list = []
    num = 0
    # print(f'text.split(): {text.split(",")}')
    for letter in text_list[2:text_length-2]:
        if num % 2 == 0:
            letter_list.append(letter)
        num += 1
    result = ''.join(letter_list)
    return ''.join(letter_list)


def real_text_filter_in_not_s(contact_info_html):
    span_list = contact_info_html.find_all('span')
    real_text_list = []
    for span in span_list:
        if span.has_attr('style'):
            print('')
        else:
            print(f'span: {span}')
            real_text_list.append(span.text)

    print(f'real_text_list: {real_text_list}')

    real_text = ''.join(real_text_list)
    print(f'real_text: {real_text}')

    phone_num_list.append(real_text)

    print(f'phone_num_list: {phone_num_list}')

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

floor_num = 1

shop_list_bulk = floor_list[floor_num].find('ul')
shop_list = shop_list_bulk.find_all('li')

# print(f'shop_list num: {len(shop_list)}')

shop_url = shop_list[4].find('a')['href']
html = s.get(f'https://www.vvic.com{shop_url}', headers = headers).text
bs = bs4.BeautifulSoup(html, 'html.parser')

# print(f'bs div num: {len(bs.find_all("div"))}')

body = bs.find('body')
div_list = body.find('div', class_='w clearfix shop-wrap')
shop_content = div_list.find('div', class_='shop-content shop-content-top')
mt10 = shop_content.find('ul', class_='mt10')
shop_contact_list = mt10.find_all('li')

# print(f'shop_contact_list: {shop_contact_list}')

# print(f'shop_contact_list: {shop_contact_list}')

shop_info = []
shop_phone = ''
shop_wechat = ''
shop_qq = ''

for li in shop_contact_list:

    li_attr_text = li.find("div", class_="attr").text
    li_text_list = []

    phone_num_list = []
    li_text = li.text.split("：")[1].split()
    # real_text_list
    # if (li_attr_text == '电话：'):
    #     letter_list_list = li.find_all("p")
    #     print(f'letter_list_list: {letter_list_list}')
    #     for letter_list in letter_list_list:
    #
    #         span_list = letter_list.find_all('span')
    #         real_text_list = []
    #         for span in span_list:
    #             if span.has_attr('style'):
    #                 print('')
    #             else:
    #                 print(f'span: {span}')
    #                 real_text_list.append(span.text)
    #
    #         print(f'real_text_list: {real_text_list}')
    #
    #         real_text = ''.join(real_text_list)
    #         print(f'real_text: {real_text}')
    #
    #         phone_num_list.append(real_text)
    #
    #     print(f'phone_num_list: {phone_num_list}')


    # if (li_attr_text == '微信：'):
    #     span_list = li.find_all('span')
    #     real_text_list = []
    #     for span in span_list:
    #         if span.has_attr('style'):
    #             print('')
    #         else:
    #             print(f'span: {span}')
    #             real_text_list.append(span.text)
    #
    #     print(f'real_text_list: {real_text_list}')
    #
    #     real_text = ''.join(real_text_list)
    #     print(f'real_text: {real_text}')
    #
    #     phone_num_list.append(real_text)
    #
    #     print(f'phone_num_list: {phone_num_list}')


    if (li_attr_text == 'QQ：'):
        real_text_filter_in_not_s(li)

    #
    # shop_info.append(shop_phone)
    # shop_info.append(shop_wechat)
    # shop_info.append(shop_qq)