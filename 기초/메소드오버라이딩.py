# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # __init__은
        self.name = name # 멤버변수
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2} ]"\
            .format(self.name,location,self.speed))
      
#공격 유닛
class AttackUnit(Unit): # Unit을 상속
    def __init__(self,name,hp,damage,speed):
        Unit.__init__(self,name,hp,speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. 공격력은 [{2}] 입니다."\
            .format(self.name,location,self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if self.hp <= 0:
            print("{0} : 파괴 되었습니다.".format(self.name))

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name, hp,0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self,location):
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

# 발키리 생성
# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name,"3시")

# 벌처
vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀 크루저
battleCrusier = FlyableAttackUnit("배틀쿠르저", 500, 25, 3)

vulture.move("11시")
# battleCrusier.fly(battleCrusier.name,"9시")
battleCrusier.move("9시")