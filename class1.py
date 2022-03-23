# class1.py 
#클래스 정의
class Person:
    #초기화 메서드(가장 먼저 수행되는 생성자 메서드)
    def __init__(self):
        self.name = "default name"

    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person()
p1.print()
p2.print()

    