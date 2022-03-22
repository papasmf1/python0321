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


