# 내장함수 
#sum, any, all,  chr, ord , bin , oct, hex, isinstance , round ...  너무 많아서 다 다룰 순 없고 상황에 맞게 적용해서 쓰면 됨
 

# 사용자 함수 
# 파라미터(함수에 인풋 데이터를 전달하기 위한 변수)에 *args, **kwargs

def 함수명():
    print("함수호출")
    return True

a = 함수명()


c = 10

def add(a,b) :
    global c     # 전역변수 c를 가져다 쓰겠다는 의미
    c = a + b
    return c

b = add(1, 10)
print(b,c)

# 매개변수에서 타입을 지정해줄 수 있다 -> def get_input_user(msg, casting = int) :
def get_input_user(msg, casting) :
    ''' 사용자에게 msg를 출력하고 casting 형태를 확인하여 입력된 값을 리턴합니다. 
    
    Args:
        msg (str) : input시 출력할 문구
        casting (class) : 사용자에게 입력 받은 값의 자료형
    
    Returns: 
        user (casting-value) : 사용자에게 입력받은 값
    '''
    while True:
        try: 
            user = casting(input(msg))
            return user
        except:
            continue
        
user = get_input_user("사용자 이름을 입력하세요.", str)
age = get_input_user("사용자 나이를 입력하세요.", int)

def save_winner (*args):
    print(args)
    
def save_winner2 (**kwargs):
    print(kwargs)
    if kwargs.get("name1"):
        print(kwargs["name1"])

    
save_winner("김가나")
save_winner("김가나", "김다라", "김마바")
save_winner2(name1 ="김가나", name2="김다라")

def outer_function(func):
    def inner_function(*args, **kwargs):
        print("함수명 : {}".format(func.__name__))
        print("args : {}".format(args))
        print("kwargs : {}".format(kwargs))
        result = func(*args, **kwargs)
        print("result : {}".format(result))
        return result
    return inner_function

def add(a,b):
    return a+b

f = outer_function(add)
f(10,20)        