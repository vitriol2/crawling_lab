import selenium
from selenium import webdriver
import time
import bs4
import csv
from urllib.request import urlopen
import requests

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
def text_split(content):
    # print(f'content: {content}')
    text = str(content)
    text_list = list(text)
    text_length = len(text_list)
    # print(f'text: {text}')
    letter_list = []
    num = 0
    # print(f'text.split(): {text.split(",")}')
    for letter in text_list[1:text_length-2]:
        if num % 2 == 0:
            letter_list.append(letter)
        num += 1
    result = ''.join(letter_list)
    return ''.join(letter_list)

def real_text_filter_in_not_s(contact_info_html):

    span_list = contact_info_html.find_all('span')
    real_text_list = []
    for span in span_list:
        if not span.has_attr('style'):
            real_text_list.append(span.text)

    real_text = ''.join(real_text_list)

    return real_text

# chromedriver_dir = r'/Users/apple/Documents/crawling/chromedriver'
# driver = webdriver.Chrome(chromedriver_dir)
# # driver.delete_all_cookies()
#
# driver.get('https://www.vvic.com/gz/shops/12')
# #
shop_info_list = []


# floors_bulk = driver.find_element(By.CLASS_NAME, 'mk-shops.mt10')
# floor_list = floors_bulk.find_elements(By.CLASS_NAME,'stall-table.clearfix')
# # print(len(floor_list))

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

domain = 'https://www.vvic.com'

street = 49

s = requests.Session()
url = f'https://www.vvic.com/gz/shops/{street}'
html = s.get(url, headers = headers).text
# html = urlopen(url).read()
soup = bs4.BeautifulSoup(html, 'html.parser')

floor_bulk = soup.find('div', class_="mk-shops mt10")
floor_list = floor_bulk.find_all('dl', 'stall-table clearfix')

floor_num = 1

# shop_list_bulk = floor_list[floor_num].find_element(By.TAG_NAME, 'ul')
# shop_list = shop_list_bulk.find_elements(By.TAG_NAME, 'li')


shop_list_bulk = floor_list[floor_num].find('ul')
shop_list = shop_list_bulk.find_all('li')

# print(f'shop_list[0]: {shop_list[0].find_element(By.TAG_NAME, "a").get_attribute("href")}')
print(f'shop_list num: {len(shop_list)}')
# print(f'shop_list : {shop_list}')

# shop = shop_list[0]


# 샵 정보 보기

shop_num = 0
# 에러로인해 중간부터 다시
# for shop in shop_list[126:]:
# 처음부터
for shop in shop_list:
    if shop_num == len(shop_list)-1:
        break
    # print(f'shop_num: {shop_num}')
    shop_info = []
    # print(f'shop.text: {shop.text}')
    shop_info.append(shop.text)

    # shop_page = shop.find("a")["href"]
    # print(f'shop_page: {domain}{shop_page}')
    # html = urlopen(f'{domain}{shop_page}').read()
    # # html = s.post(f'{domain}{shop_page}').text
    # # print(f'html: {html}')
    # bs = bs4.BeautifulSoup(html, 'html.parser')

    try:

        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(60)

        shop_url = shop.find('a')['href']
        html = s.get(f'https://www.vvic.com{shop_url}', headers = headers).text
        bs = bs4.BeautifulSoup(html, 'html.parser')

        try:


            body = bs.find('body')
            div_list = body.find('div', class_='w clearfix shop-wrap')
            shop_content = div_list.find('div', class_='shop-content shop-content-top')
            mt10 = shop_content.find('ul', class_='mt10')
            shop_contact_list = mt10.find_all('li')

            phone_num_list = []
            shop_phone = ''
            shop_wechat = ''
            shop_qq = ''
            # print(f'shop_contact_list[2].attr: {shop_contact_list[2].find("div", class_="attr")}')

            # :와 ：가 다름, 후자는 직접 페이지에서 복사해온 것
            for li in shop_contact_list:
                li_attr_text = li.find("div", class_="attr").text
                li_text_list = []

                # print(f'li.text.split("：")[1]: {li.text.split("：")[1]}')

                # num = 0
                # for letter in li.text.split('：')[1].split['']:
                #     if num % 2 == 0:
                #         li_text_list.append(letter)
                # li_text = ''.join(li_text_list)
                # print(f'li_attr_text: {li_attr_text}')
                li_text = li.text.split("：")[1].split()
                # print(f'li_text: {li_text}')

                if (li_attr_text == '电话：'):
                    letter_list_list = li.find_all("p")
                    # print(f'letter_list_list: {letter_list_list}')

                    for letter_list in letter_list_list:
                        phone = real_text_filter_in_not_s(letter_list)
                        # print(f'phone: {phone}')
                        phone_num_list.append(phone)

                    # print(f'phone_num_list: {phone_num_list}')

                if(li_attr_text == '微信：'):
                    shop_wechat = real_text_filter_in_not_s(li)
                if(li_attr_text == 'QQ：'):
                    shop_qq = real_text_filter_in_not_s(li)


            shop_info.append(phone_num_list)
            shop_info.append(shop_wechat)
            shop_info.append(shop_qq)

            shop_info_list.append(shop_info)

            shop_num += 1
        except AttributeError:
            try :

                signal.signal(signal.SIGALRM, alarm_handler)
                signal.alarm(60)

                shop_contact = bs.find('div', class_='shop-info-con')
                shop_contact_list = shop_contact.find_all('div', class_='contact-info')
                # print(f'shop_contact_list[1]: {shop_contact_list[1]}')

                shop_phone = ''
                shop_wechat = ''
                shop_qq = ''
                for contact in shop_contact_list:
                    contact_category = ''.join(list(contact.text)[:3])
                    # print(f'contact_category: {contact_category}')
                    if contact_category == '电话：':
                        contact_full_text_list_length = len(list(str(contact.text)))
                        shop_phone = ''.join(list(str(contact.text))[18:contact_full_text_list_length - 13])

                    if contact_category == '微信：':
                        contact_full_text_list_length = len(list(str(contact.text)))
                        shop_wechat = ''.join(list(str(contact.text))[3:])

                    if contact_category == 'QQ：':
                        contact_full_text_list_length = len(list(str(contact.text)))
                        shop_qq = ''.join(list(str(contact.text))[3:])



                shop_info.append(shop_phone)
                shop_info.append(shop_wechat)
                shop_info.append(shop_qq)
                shop_info.append('s')

                shop_info_list.append(shop_info)

                shop_num += 1
            except AttributeError:
                print(f'AttributeError shop_num: {shop_num}')

                shop_info_list.append(shop_info)
                shop_num += 1
            except TimeoutException:
                print(f'TimeoutException shop_num: {shop_num}')

        except selenium.common.exceptions.TimeoutException:
            print(f'TimeoutException shop_num: {shop_num}')

        # except :
        #     print(f'except shop_num: {shop_num}')
        #     shop_info_list.append(shop_info)
        #     break

        print(f'shop_info: {shop_info}')

    except selenium.common.exceptions.TimeoutException:
        print(f'TimeoutException shop_num: {shop_num}')


# csv파일을 새로 작성할 때
f = open(f'shop/{street}_shopList_floor_{floor_num}.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in shop_info_list:
    csvWriter.writerow(i)


# # //에러로인해서 추가를할 때
# f = open(f'shopList_floor_{floor_num}.csv', 'a', encoding='utf-8', newline='')
# csvWriter = csv.writer(f)
# for i in shop_info_list:
#     csvWriter.writerow(i)

f.close()
