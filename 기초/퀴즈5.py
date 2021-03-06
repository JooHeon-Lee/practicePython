#조건 1 : 승객별 은행 소요 시간은 5~50분 사이의 난수 
#조건 2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

#출력문 예제
#[0] 1번째 손님 ( 소요시간 : 15분)
#[] 2번째 손님 (소요시간 : 50분)
#[0] 3번째 손님 (소요시간 : 5분)
#...
#[] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2분
from random import *

time = 0
index = 0 # 총탑승 승객
for i in range(1,51):
    time = randint(5,50)
    if 5 <= time <=15: # 매칭성공
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
        index += 1
    else: # 매칭실패
        print("[] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
print("총 탑승 승객 :  {0}분".format(index))