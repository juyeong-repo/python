#파일 읽고 쓰기

file = open("sample.txt", mode = "w", encoding = "utf-8")
file.write("hello python")
#클로즈하지 않으면 다른 프로그램이나 객체에서 접근하지 못하는 현상 발생 가능 
file.close()

rfile = open("sample.txt", mode="r", encoding="utf-8")
#반복문으로 한줄씩 빼거나 readLine 함수 이용하여 데이터 읽을 수 있음 
#content = rfile.read()

# a = rfile.read(10)
# rfile.close()
# print(content)

with open("sample.txt", mode="r", encoding= "utf-8") as s, open("sample.txt", mode="w", encoding= "utf-8") as t :
    t.wrtie(s.read().replace("파이썬", "python"))