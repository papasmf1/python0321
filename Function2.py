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

#불변형식인 전역변수에 읽기+쓰기까지 하는 경우
g = 1 
def testScope(a):
    #global g 
    #지역변수를 초기화(우선적으로 사용)
    g = 2 
    return a+g 

#호출
print(testScope(1))
print("전역변수 g:", g)


#디버깅 연습(교집합으로 되어 있는 문자를 출력)
def intersect(prelist, postlist):
    #지역변수에 겹치는 글자를 모아두가 
    retList = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #and연산자는 ~이면서 ~이고 
        #"A"라는 글자가 postlist에 포함되어 있고 그리고 "A"글자가 아직 없다. 
        # in(포함되어있음) not in(포함되어있지 않다)
        if x in postlist and x not in retList:
            retList.append(x)
    return retList 

#호출
print(intersect("HAM","SPAM"))
