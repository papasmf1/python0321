# Function2.py 
#가변형식
wordlist = ["J","A","M"]

#함수를 정의
def change(x):
    x[0] = "H"

#함수를 호출
change(wordlist)
#변수를 출력
print(wordlist)

print("---약간 수정----")
wordlist = ["J","A","M"]

#함수를 정의
def change(x):
    #지역변수에 복사
    x1 = x[:]
    x1[0] = "H"
    print("함수내부:", x1)

#함수를 호출
change(wordlist)
#변수를 출력
print(wordlist)

#함수의 내부 이름 해석(LGB)
x = 1
def func1(a):
    return a+x 

#호출
print(func1(1))

def func2(a):
    x = 2 
    return a+x 

#호출
print(func2(1))

