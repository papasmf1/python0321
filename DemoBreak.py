#DemoBreak.py 

lst = [1,2,3,4,5,6,7,8,9,10]

for item in lst:
    #블럭 주석 처리: ctrl + / 
    if item > 5:
        break 
    print("item:{0}".format(item))


print("---continue---")

for item in lst:
    if item % 2 == 0:
        continue
    print("item:{0}".format(item))

#수열함수를 사용
print(list(range(10)))
print(list(range(1,11)))
years = list(range(2000, 2023))
print(years)

#수동으로 10번 반복
for i in range(5):
    print(i)


#리스트 내장
lst = [1,2,3,4,5,6,7,8,9,10]

result = [item**2 for item in lst if item > 5]
print(result)

colors = {100:"apple", 200:"banana", 300:"kiwi"}
print([v.upper() for v in colors.values()])

#필터링하는 함수
lst = [10,25,30]

itemL = filter(None, lst)
for item in itemL:
    print(item)

print("---필터링하는 경우---")
#필터링 함수 정의
def getBiggerThan20(i):
    return i>20

itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)
