#클래스 = 함수 + 변수
class Person:
    def __init__(self,name,age): #오브젝트 생성시 name의 인자를 받아서 변수에 넣어라
        self.name = name
        self.age = age

    def say_hello(self, to_name): # to_name이라는 인자를 받음
        print("안녕!{0}, 나는 {1}".format(to_name,self.name))

    def introduce(self):
        print("내 이름은 {0}, 그리고 나는 {1}살이야".format(self.name,self.age))
# a = Person("주헌")
# b = Person("마이클")
# c = Person("둥이")

# a.say_hello("철수")
# b.say_hello("영희")
# c.say_hello("미지")

a = Person("주헌","25")
a.introduce()

#=======상속===========

class Police(Person):# 괄호안에 클래스를 넣으면 폴리스가 펄슨을 상속한다라는의미
    def arrest(self,to_arrest):
        print("넌 체포됐다, {0}".format(to_arrest))

class Programmer(Person):
    def program(self,to_program):
        print("이번에는 {0}를 만들어야 겠다".format(to_program))

jooheon = Person("주헌","25")
jenny = Police("제니","20")
michael = Programmer("마이클","22")

jooheon.introduce()
jenny.introduce() # 폴리스가 person을 상속해서 person에 있는 함수를 다 쓸수있음
michael.introduce()
jenny.arrest("주헌")
michael.program("이메일 클라이언트")