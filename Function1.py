# Function1.py 

#리턴을 하지 않는 경우
def setValue(x):
    print("내부에서 출력:", x)

#함수를 호출 
retValue = setValue(5)
print(retValue)

#리턴을 여러개 하는 경우
def swap(x,y):
    return y,x

#함수를 호출
retValue = swap(5,6)
print(retValue)

#가변형식과 불변형식 
#불변형식(정수,실수,불린,문자열,튜플)
#값형식은 없고 참조형식만 제공 
a = 5 
print(id(a))
a = 6 
print(id(a))

print("---가변형식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

print(globals())


