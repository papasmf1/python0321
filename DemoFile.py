# DemoFile.py 

import sys 

#print("hello", "python", sep="~", end="!", file=sys.stderr)

print("hello\nworld")

URL = "http://www.credu.com/?page=" + str(1) 
print(URL)

#문자열 정렬
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(3))

#binary(b), hex(x), c(character) ASCII코드 테이블
print("---2진수,16진수 출력(서식문자)---")
print("{0:b}".format(10))
print("{0:x}".format(10))
print("{0:c}".format(65))
#엑셀 서식(화폐, 돈)
print("{0:,}".format(15000))



