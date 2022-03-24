# web2.py
#웹서버와 통신 
import urllib.request
#크롤링 
from bs4 import BeautifulSoup

data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
soup = BeautifulSoup(data, 'html.parser')

#ctrl + /: 직접 분석  
# <td class="title">
# 	<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri">마음의 소리 50화 <격렬한 나의 하루></a>
# </td>

#<td> 10개 
cartoons = soup.find_all("td", class_="title")
print(len(cartoons))

#슬라이싱
title = cartoons[0].find('a').text
link = cartoons[0].find('a')['href']
print(title)
print(link)

#파일로 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for item in cartoons:
    title = item.find('a').text
    print(title)
    f.write(title + "\n")

f.close() 


