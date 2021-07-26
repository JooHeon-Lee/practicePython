#지역변수 함수내 
#전역변수 프로그램내

gun = 10

def checkpoint(soldiers): # 경계근무 나가는 군인 수
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))
