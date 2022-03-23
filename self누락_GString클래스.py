#이름이 충돌하는 경우 
#전역변수 
str = "Not Class Member"

#파이썬은 모호한 것 보다는 명확하게 코딩 
class GString:
    def __init__(self):
        #멤버 변수 
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #약간의 실수 
        print(self.str)

g = GString()
g.set("First Message")
g.print()
