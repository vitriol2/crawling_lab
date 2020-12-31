from selenium import webdriver
import time
import bs4
import csv

chromedriver_dir = r'/Users/apple/Documents/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver_dir);

driver.get('https://www.starbucks.co.kr/store/store_map.do')

time.sleep(5)

loca = driver.find_element_by_class_name('loca_search')
loca.click()


time.sleep(2)

sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li')
li[0].click()

time.sleep(2)

gugun = driver.find_element_by_class_name('gugun_arae_box')
guli = gugun.find_element_by_tag_name('li')
print(guli.text)
guli.click()

#
# time.sleep(2)
#
# source = driver.page_source
# bs = bs4.BeautifulSoup(source, 'html.parser')
# entire = bs.find('ul', class_='quickSearchResultBoxSidoGugun')
# li_list = entire.find_all('li')
#
# cafeList = []
# for i in li_list:
#     # print(i.find('strong').text)
#     temp = []
#     temp.append(i.find('p').text)
#     temp.append(i.find('strong').text)
#     cafeList.append(temp)
#
#
# f = open(f'starbucks_cafe.csv', 'w', encoding='utf-8', newline='')
# csvWriter = csv.writer(f)
#
# for i in cafeList:
#     csvWriter.writerow(i)
#
# f.close()
#
# print('완료되었습니다.')