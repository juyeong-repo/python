# for 순차적인 요소


a = "abcdefg"
for i in a:
    print(i)
    
# 0,, 1,2, ... 99까지 찍힘     
for i in range(100):
    print(i)

# 1,2,3,4,5
for i in range(1, 6):
    print(i)

# 1,3,5,7,9 (2씩 점프)
for i in range (1,10,2):
    print(i)
    

#1,2,3,4,5,6
a = [(1,2), (3,4), (5,6)]
for i in a: 
    for j in i:
        print (j)


# for, enumerate (인덱스 구할 때 많이 사용)
student =[{"홍길동": 100}, {"가제트": 200}, {"가가멜": 300}]

# s=갯수, i=요소(student)
for s, i in enumerate(student, start=1):
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("{} 이름: {} 점수: {}".format(s, name, value))
    

# comprehension

result = []
for num in range(1,6):
    result.append(num + 5)
print(result) #6,7,8,9,10


result = [num+5 for num in range(1,6)]
print (result)


# 
result = [num *3 for num in range(1,99) if num %2 == 0]
print (result)


for num in range(1,99) :
    if num % 2 == 0:
     result.append(num*3)
     

#구구단
for i in range (2,10):
    for j in range (1,10):
        result = i * j
        print ("{} x {} = {}".format(i,j,result))
        

gugudan  = [i * j  for i in range(2,10) for j in range(1,10)]
print(gugudan)