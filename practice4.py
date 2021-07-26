java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

# 교집합 
print(java & python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합

print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("이주헌")
print(python)

#java를 잊었다
java.remove("김태호")
print(java)

# 자료구조의 변경
menu = {"커피","우유","주스"}
print(menu,type(menu))

menu = list(menu)
print(menu,type(menu))

menu = tuple(menu)
print(menu,type(menu))

menu = set(menu)
print(menu,type(menu))

##Quiz

from random import *

users = range(1,21) # 1부터 20까지 숫자 생성
print(type(users))
users = list(users)
print(users)
shuffle(users)
print(users)
winners = sample(users,4) # 치킨당첨자 무작위 한명 커피 세명

print("---- 당첨자 발표 ----")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("---- ㅊㅋ ----")
