# Function3.py

#기본값을 주는 경우
def times(a=5,b=20):
    return a*b 

#호출
print(times())
print(times(2))
print(times(2,3))

#키워드인자(파라메터명을 지정)
def connectURI(server,port):
    strURL = "http://" + server + ":" + port 
    return strURL

#호출
print(connectURI("credu.com","80"))
print(connectURI(port="8080", server="credu.com"))


