import csv
from urllib.request import urlopen

# 한글 인코딩
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

url = f'https://www.vvic.com/gz?noCity=1'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

total = soup.select('.item')
marketList = []

for i in total:
    temp = []
    temp.append(i.text)
    marketList.append(temp)

f = open(f'market_list.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in marketList:
    csvWriter.writerow(i)

f.close()

print('완료되었습니다.')