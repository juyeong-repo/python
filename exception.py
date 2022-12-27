# 예외처리 try / except

try:
    val = "10.5"
    n = int(val)
except:
    print("오류발생")
    
    
    
try:
    idx = []
    idx[0] = 100
except Exception as e:
    print("오류발생 {}".format(e))
finally:
    print("정상출력")
#finally는 예외 발생 여부 상관없이 실행 됨    
    
try:
    idx = []
    idx[0] = 100
except:
    pass

print("OK")

