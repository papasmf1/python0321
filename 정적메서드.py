# 정적메서드.py
class MyCalc:
    #살이있는 주석, 장식(데코레이터)
    @staticmethod
    def my_add(x,y):
        return x+y

#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)


