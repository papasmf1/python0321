# DemoRE.py 
import re 

#print(dir(re))

#search함수를 처음부터 끝까지 검색 
result = re.search("[0-9]*th", "35th")
print(result)
#match함수는 처음부터 정확하게 일치 
result = re.match("[0-9]*th", "35th")
print(result)

