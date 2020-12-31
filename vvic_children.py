import csv
from urllib.request import urlopen

# 한글 인코딩
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# url = f'https://www.vvic.com/gz/shops/12'
url = f'https://www.vvic.com/gz/shops/12'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# tag = "<p class='youngone' id='junu'> Hello World! </p>"
# soup = BeautifulSoup(tag,  'html.parser')

# 태그 이름만 특정
# 사이트 탐색기에서 class라고 써져있는 것을 넣어도 안될 때가 있다. 그럴때는 직접 위의 soup를 분석해서 원하는 부분의 진짜 class명이 뭔지 확인해야 한다.
total = soup.select(".items.j-vct.items-strength")
# print(len(total))




shopIdList = []

for i in total:
    temp = []
    # temp.append(i.text)
    temp.append(i.attrs['data-id'])
    shopIdList.append(temp)

# print(shopIdList)

f = open(f'shopIdList.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in shopIdList:
    csvWriter.writerow(i)

f.close()

print('완료되었습니다.')