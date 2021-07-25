print(5);
print('문자열');
print("d"*5);
# 참 / 거짓
print(5 > 10);

#변수 테스트 print에서 사용시 str()으로 형변환 해줘야함.
name ="이주헌";
type="사람";
age = 25;

print(name + "의");
print("나이는 ?" + str(age));

# 이거는 한줄 주석
'''이거는 여러줄 주석''' 
station = "사당";
print(station+"행 열차가 들어오고있습니다.");

#연산자
print(1+1); #2
print(3-2); #1
print(5*2); # 10
print(6/3); #2
print(2**3); #2^3
print(5%3); # 2 -> 나머지
print(5//3); #1 -> 몫

#숫자처리함수
print(abs(-5)); #5 -> 절댓값
print(pow(4,2)); #4^2 = 4*4 = 16
print(max(5,12)); # 12 -> 최댓값
print(min(5,2)); # 2 -> 최솟값
print(round(3.14)); #3
print(round(4.99)); #5 가까운수 반올림

from math import *
print(floor(4.99)); #내림.
print(ceil(3.14)); #올림.
print(sqrt(16)); # 제곱근 = 4

#랜덤함수
from random import *

print(random()); #0.0 ~ 1.0미만의 임의의 값 생성
print(random() * 10); # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10));# 0~ 10 미만의 임의의 값 생성
print(int(random() * 10));# 0~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1 );# 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 45) + 1 );# 1 ~ 45 이하의 임의의 값 생성
print(randrange(1,45)); # 1 ~ 45 미만의 임의의 값 생성
print(randint(1,45));# 1 ~ 45이하의 임의의 값 생성

#퀴즈 월 4회 스터디, 3번 온라인 1번 오프라인 
#조건 1 : 랜덤으로 날짜 뽑기
#조건 2 : 월별 날짜는 다름 최소 일수인 28이내로 정함
#조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
#출력문 : 오프라인 스터디 모임 날짜는 매월x일로 선정되었습니다.

#from random import *
dt = randint(4,28); # 4일~ 28일 미만으로 정함.
print(dt)
dt = list(str(dt))
print(dt)
print("오프라인 스터디 모임 날짜는 매월 " + str(dt) + "일로 선정되었습니다.");