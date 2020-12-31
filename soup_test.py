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
# total = soup.find('a', class_="items")
total = soup.select(".items.j-vct.items-strength")
print(len(total))

# # 태그 속성만 특정
# soup.find(class_='youngone')
#
# soup.find(attrs = {'class':'youngone'})
#
# # 태그 이름과 속성 모두 특정
# soup.find('p', class_='youngone')
