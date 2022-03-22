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




