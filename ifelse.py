# ifelse.py 

#input()함수를 무조건 문자열을 리턴
#정수로 변환 int() 
#블럭으로 주석처리: ctrl + / 
# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

#반복구문
value = 5 
while value > 0:
    print(value)
    value -= 1 

print("----실행종료----")

#시퀀스형식(List, Tuple, Str)
for i in [100, "apple", 200]:
    print(i, type(i))

#for in은 자동으로 아이템을 나열 a(0) | b(1) | c(2)
for c in "abc":
    print(c)

for item in [100,200,300]:
    print(item)

#구구단 출력
#Outer(바깥쪽 반복)
for i in [2,3,4,5,6]:
    #{0} 위치를 지정해서 변환 
    print("---{0}단 출력---".format(i))
    #Inner(안쪽 반복)
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i, j, i*j))


#삼각형 출력 
for i in [1,2,3,4,5,6,7,8,9,10]:
    print("*" * i)


