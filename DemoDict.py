# DemoDict.py
device = {"아이폰":5, "아이패드":10, "윈도우":20}

for item in device.items():
    print(item)

for key in device.keys():
    print(key)

for value in device.values():
    print(value)

#검색
print(device["아이폰"])
#수정
device["아이폰"] = 6 
#입력
device["맥북m1"] = 15 
#삭제
del device["아이폰"]
print(device)

print("----전화번호관리----")
phone = {"kim":"1111","lee":"2222","park":"3333"}
p = phone
print( id(phone), id(p) )
p["kang"] = "1234"
print(phone)
print(p)



