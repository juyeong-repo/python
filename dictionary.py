#dictionary

a = {}
a  {"키" : "값"}

#json과 같은 형태
#키는 중복될 수 없다. 

a = { "name" : "홍길동" }
b = { "age" : 30}
c = { "country" : "한국"}

a.update(b)
# >>> {'name': '홍길동', 'age' : 30}

a = {"친구들" : ["홍길동", "가가멜"]}
 
# update하면 뒤에 추가됨
a = {"홍길동" : "도적", "가제트" : "형사", "아즈라엘" : "고양이"}

 
#keys 는 반복문과 함께 유용하게 사용
a.keys()
# >>> dict_keys(['홍길동', '가제트', '아즈라엘'])
a.values()
# >>> dict_keys(['도적', '형사', '고양이'])
a.items()
# >>>키와 값 모두 가져옴/ dict_items([('홍길동' : '도적', '가제트' : '형사', '아즈라엘' : '고양이')])
a.get()
# get(x) :  x라는 Key에 대응되는 Value를 리턴

# "홍길동" in a 
# true, false 리턴