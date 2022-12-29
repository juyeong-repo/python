# 클래스 : 함수보다 큰 기능을 하나로 모음.. 


# __init__ (self) : 생성자 구현 코드, 객체를 호출할 때 실행된다. 
# 클래스의 멤버함수와 변수에는 항상 self가 붙어야한다. 
# '__'는 클래스 외부에서 접근할 수 없게 할 때 보통 사용한다.  ex.__init__ 
# __str__ : 클래스가 print()에 의해 출력될때 실행
# __del__ : 클래스를 메모리상에서 해지할 때 사용

class FishCakeMaker: 
    def __init__(self, param):
        self._fish_name = param
        pass 
    def show_name(self):
        print(self._fish_name)
        
    
fish = FishCakeMaker("붕어빵")
fish.show_name()



class FishCakeMaker: 
    def __init__(self, **kwargs):
        self._size = 10
        self._flavor = "팥"
        self._price = 100
        if "size" in kwargs:
            self._size = kwargs.get("size")
        if "flavor" in kwargs:
            self._flavor = kwargs.get("flavor")
        if "price" in kwargs:
            self._price = kwargs.get("price")
    def __del__ (self):
        print("삭제 되었습니다.")
    def __str__(self):
        return "<class FishCakeMaker (size = {}, price={}, flavor={})>".format(self._size, self, self._flavor ,self._price)
        
    def show(self):
        print("붕어빵 종류 {}".format(self._flavor))
        print("붕어빵 크기 {}".format(self._size))
        print("붕어빵 가격 {}".format(self._price))
        print( "*" * 60)


# 상속
class MarketGoods (FishCakeMaker):
    def __init__(self, margin = 1000, **kwargs):
        super().__init__(**kwargs)
        self._market_price = self._price + margin
    def show(self):
        print(self._flavor, self._market_price)
    
fish1 = MarketGoods(size=20, price=500)
fish1.show()