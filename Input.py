# 사용자 입력받기 -> 문자열로 인식된다.

user = input("사용자 이름을 입력하세요.")
print(user)

langs = ["한국어", "English"]
for i, l in enumerate (langs,start = 1):
    print("{}.{}".format(i, l))
  
while True:    
    sel = int(input("언어를 선택하세요. >")) 
    
    if not sel.isnumeric():
        continue
    sel = int(sel)
    
    if 0 < sel < 3:
        break
print("사용자가 선택한 언어는 {}입니다.".format(langs[sel-1]))


# 입력한 숫자가 소수인지 (소수: 자기자신과 1을 약수로 가짐) -방법1 

while True:
    num = input("숫자를 입력하세요.>")
    if not num.isnumeric():
        continue
    num = int(num)
    if num < 2:
        continue
    break
    
isPrime = True
for n in range (2, num) :
    if num % n == 0: #다른 정수로 나눠 떨어지면
        isPrime = False
        break
    
if isPrime:
    print("소수 입니다.")
else:
    print("소수가 아닙니다.")

    

# 입력한 숫자가 소수인지 - 방법2 
prime_list = [False, False] + [True] * (num - 1)
primes = []

for i in range(2, num+1):
    if prime_list[i] :
        for j in range(2*i, num+1, i):
            prime_list[j] = False
            
            
primes = [i for i in range(2, num+1) if prime_list[i] == True]
print(primes)

if num in primes: 
    print("소수입니다.")
else: 
    print("소수가 아닙니다.")
