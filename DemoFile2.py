# DemoFile2.py 

#파일을 생성
#유니코드로 쓰기와 읽기(인코딩방식을 utf-8) <----> ANSI(영문기준)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")

#쓰기
f.write("첫번째\n두번째라인\n세번째\n")
#작업을 종료(버퍼를 비우고 읽기나 쓰기를 완료)
f.close()

#읽기
f = open("c:\\work\\demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
print("---readline()---")
#파일 포인터가 어디? 
print(f.tell())
#처음으로 돌아가(리셋)
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")
f.close() 

#첨부연산(기존파일에 추가): append + read + write 모드값
f = open("c:\\work\\demo.txt", "a+", encoding="utf-8")
f.write("새로운 문자열을 추가\n")
f.close() 

#다시 읽기 
f = open("c:\\work\\demo.txt", "a+", encoding="utf-8")
print(f.read())

