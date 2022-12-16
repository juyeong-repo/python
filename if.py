# if , else, elif
# 들여쓰기 : 공백, 탭 가능하나 한 파일에선 규칙 통일해야한다. 


# 현재 시간이 12시면 점심을 먹고 아니면 일을 한다.add()

time = 12
if time == 12: 
    print("점심 먹으러 감")
else:
    print('일하는 중')
    

if 12 <=time <1 :
    print('점심 냠')
else :
    print('일하는 중')
    

# 현재 시간이 12시부터 1시이전이면 점심을 먹고 3시부터 4시까지는 휴식하고 아니면 일을 한다.

time = 12
if 12 <= time < 1:
    print('점심')
elif 3<= time <=4 :
    print('휴식')
else: 
    print('일') 
    
    
    
# 아프지 않고 현재 시간이 12시부터 1시이전이면 점심을 먹고 
# 3시부터 4시거나 아프면 휴식하고
# 아니면 일을 한다.

time = 12
seek = True

if 12 <= time < 1 and not seek:
    print('점심')
elif 3<= time <=4 or seek :
    print('휴식')
else: 
    print('일') 
    
    

a= 10
if a > 10:
    ret = 100
elif a ==10:
    ret = 200
else:
    ret = 500

ret = {a > 10 : 100, a<10: 500}.get(True, 200)
ret = {True : 100, False: 500}.get(True, 200)

# {}.get(True, 기본값)인 경우
#{}에서 True 값을 구해 리턴하는데
# True 가 없는 경우 기본값으로 200을 리턴하게 됩니다. 

