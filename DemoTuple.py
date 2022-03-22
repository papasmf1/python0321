a = {1,2,3,3}
b = {3,4,4,5}

print(a)
print(b)

#중지점(Break Point)  
print(a.union(b))
print(a.difference(b))


#튜플 사용
tp = (1,2,3)
print(tp)
print(len(tp))

#함수를 정의
def calc(a,b):
    return a+b, a*b

#첫번째 컬럼 이동
#함수를 호출
print(calc(3,4))
print("-------")
result = calc(5,6)
print(result)
print(result[0], result[1])
result1, result2 = calc(2,3)
print(result1, result2)
#튜플에 묶어서 데이터를 저장 
args = (3,4)
print(calc(*args))

#형식을 변환
a = (1,2,3)
b = set(a)
print(type(b))
print(b)
c = list(b)
c.append(4)
print(c)

#변수의 값을 덮어쓰기를 한경우 
a1 = 5 
a2 = 10 
print(a1, a2)

#딕셔너리
color = {"apple":"red", "banana":"yellow"}
print(len(color))
print(type(color))
print(color["apple"])

#반복구문
for item in color.items():
    print(item)


print("------------")
for k,v in color.items():
    print(k,v)

#내가 원하는 만큼 반복 인덱싱[0,5]
#규칙이 있는 수열을 만들 때 사용: range(start, end, step)
for i in range(1,11):
    print(i)












