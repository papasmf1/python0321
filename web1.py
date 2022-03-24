# web1.py
from bs4 import BeautifulSoup

page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

#<p>태그 몽땅 
#print(soup.find_all("a"))

#첫번째 <p>만 검색
#print(soup.find("p"))

#필터링: <p class="outer-text">컨텐츠</p>
result = soup.find_all("p", class_="outer-text")
for item in result:
    strContent = item.text 
    print(strContent.strip())





