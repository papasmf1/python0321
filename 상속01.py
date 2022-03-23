#부모 클래스 정의 
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스 정의(코드 상속) 
class Student(Person):
    #상속받은 메서드를 재정의(덮어쓰기, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #부모의 생성자 호출(base, super라는 부모를 가리키는 키워드)
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #메서드 로직을 새로 작성(덮어쓰기)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, Student: {1})".format(
            self.subject, self.studentID))

            
#인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "20201122")
p.printInfo()
s.printInfo()

