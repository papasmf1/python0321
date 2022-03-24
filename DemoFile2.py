# DemoFile2.py 

#파일을 생성
#유니코드로 쓰기와 읽기(인코딩방식을 utf-8) <----> ANSI(영문기준)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")

#쓰기
f.write("첫번째\n두번째라인\n세번째\n")
#작업을 종료(버퍼를 비우고 읽기나 쓰기를 완료)
f.close()





