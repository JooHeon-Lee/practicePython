# 리스트 []

#지하철 칸별로 10명, 20명, 30명

#subway1 = 10;
#subway2 = 20;
#subway3 = 30;

# subway = [10,20,30]
# print(subway)

# subway = ["이","주","헌"]
# print(subway)

# #주는 몇번재에 있는가
# print(subway.index("주"))
# #헌 뒤에 은 추가
# subway.append("은")
# print(subway)
# #이 주 사이에 고 추가
# subway.insert(1,"고")
# print(subway)
# #뒤에서부터 추출
# print(subway.pop())

#정렬
# num_list =[5,9,5,7]
# num_list.sort()
# print(num_list)
# #뒤집기
# num_list.reverse()
# print(num_list)
# #모두지우기
# num_list.clear()
# print(num_list)

#다양한 자료형 사용
# mix_list = ["이주헌",20,True]
# print(mix_list)
# #리스트 확장
# mix_list.extend(["1","2"])
# print(mix_list)

#사전 자바의 맵과 같음
cabinet = {1:"이주헌",2:"이주헌2"}
print(cabinet[2])
print(cabinet.get(2))
print(cabinet.get(2),"이름변경가능함이렇게")

print(1 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-01":"이주헌","B-02" : "이주헌2"}
print(cabinet.get("A-01"))
print(cabinet["A-01"])
cabinet["C-03"] = "이주헌3"
print(cabinet)

del cabinet["A-01"]
print(cabinet)

# key만 출력
print(cabinet.keys())

#values 만 출력
print(cabinet.values())

#key value 둘다 출력
print(cabinet.items())

#비우기
cabinet.clear()
print(cabinet)

#튜플
menu = ("김치","단무지")
print(menu[0])
print(menu[1])

#menu.add("깎두기")

# name = "김종국"
# age = 20
# hobby = "운동"
# print(name,age,hobby)

(name, age, hobby) = ("김종국",20,"운동")
print(name,age,hobby)
