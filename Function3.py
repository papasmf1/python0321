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


#가변인자 처리
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#정의되지 않은 인자(**, 내부에서 딕셔너리)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#호출
print(userURIBuilder("credu.com","80", id="kim", passwd="1234")) 
print(userURIBuilder("credu.com","80", id="kim", passwd="1234", age="30"))
 