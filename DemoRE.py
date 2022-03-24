# DemoRE.py 
import re 

#print(dir(re))

#search함수를 처음부터 끝까지 검색 
result = re.search("[0-9]*th", "35th")
#매칭 오브젝트를 리턴 
print(result)
#match함수는 처음부터 정확하게 일치 
result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

#약간의 함정 추가
print("---패턴 매칭---")
print(bool(re.search("\d*th", "3th")))
print(bool(re.search("\d*th", "th")))
print(bool(re.match("[0-9]+th", "  35th")))

print("--우편변호 패턴---")
print(bool(re.search("\d{5}", "우리 동네는 52300")))
print("--연도 패턴---")
print(bool(re.search("\d{4}", "올해는 2022년")))
result = re.search("\d{4}", "올해는 2022년")
print(result.group())


