# try1.py
#에러 처리 추가 

#함수 정의
from typing import final


def divide(a,b):
    return a/b 

try: 
    #호출
    result = divide(5,0)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 합니다.")
else:
    print("실행결과:{0}".format(result))
finally:
    print("무조건 실행")

print("---전체 코드 실행 종료---")

