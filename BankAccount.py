# BankAccount.py

#은행의 계정을 표현한 클래스 
#멤버변수를 숨기기전 
class BankAccount:
    #초기화
    def __init__(self, id, name, balance):
        #파이썬에게 멤버를 숨겨달라(이름변경)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    #입금 메서드
    def deposit(self, amount):
        self.__balance += amount 
    #출금 메서드 
    def withdraw(self, amount):
        self.__balance -= amount
    #객체의 문자열을 처리: ToString()메서드  
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)

print(account1)
#이름규칙: _클래스명__변수명(백도어)
print(account1._BankAccount__balance)




