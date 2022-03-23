# 메모리관리.py 

class MyClass:
    #생성자 메서드(가장 먼저 실행:초기화)
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    #소멸자 메서드(가장 마지막에 실행:청소, 정리...)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성
#객체는 참조카운트(1->0)
d = MyClass(5)
#del d 

