# DemoStr.py 

print(dir(str))

strA = "python is very powerful"
print(len(strA))
print(strA.capitalize())
print(strA.count("p"))
#count("글자", start, end)
print(strA.count("p", 7))

print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isnumeric())

print("demo.ppt".endswith("ppt"))

#문자열 처리 메서드(웹상에서 파일을 불러오면 공백문자가 있는 경우) 
#화이트 스페이스(공백) - 약간의 문자열을 가공(전처리)
u = "<<<  spam and ham  >>"
print(u)
result = u.strip("<> ")
print(result)
#치환
result = result.replace("spam", "spam egg")
print(result)
#문자열을 리스트로 변환
result2 = result.split()
print(result2)
#다시 하나의 문자열로 합치기 
strJoin = ":)".join(result2)
print(strJoin)



