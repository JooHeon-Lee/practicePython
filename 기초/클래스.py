# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
#         name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)

class Unit:
    def __init__(self, name, hp, damage): # __init__은
        self.name = name # 멤버변수
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# marine1 = Unit("마린",40, 5)
# marine2 = Unit("마린",40, 5)
# tank = Unit("탱크", 150, 35)
# 레이스 : 공중 유닛, 비행기, 클로킹
wraith1 = Unit("레이스",80,5)
print("유닛 이름 : {0}.공격력 : {1}".format(wraith1.name,wraith1.damage))

wraith2 = Unit("빼앗은 레이스",80,5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))