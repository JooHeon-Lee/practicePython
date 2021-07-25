#문자열 처리
sentence = '나는 이주헌이다.';
print(sentence);
sentence2 = '파이선 쉽다'
print(sentence2);

#슬라이싱
jumin = "991201-1234567"

print("성별 : " + jumin[7]);
print("년도 : " + jumin[0:2]); # 0부터 2 직전까지 즉 0번째랑 1번째
print("월 : " + jumin[2:4]); # 2,3번째
print("일 : " + jumin[4:6]);

print("생년월일 : " + jumin[0:6]);
print("주민 뒷자리 : " + jumin[-7:]); # 뒤에서 7자리

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower()); #소문자 처리
print(python.upper());# 대문자 처리
print(python[0].isupper()); # 0번째가 대문자인지 체크
print(len(python));#문자열 길이(공백포함)
print(python.replace("Python","Java"));# 문자열 대체

index = python.index("n"); #문자열중 n의 위치
print(index);
index = python.index("n", index+1);
print(python[index])
print(python.index("n", 8));

print(python.find("n")); # 있으면 위치 반환 없으면 -1 반환
#print(python.index("dd")); #없으면 오류남

#문자열 포맷
#print("a" + "b"); # ab
#print("a","b");# a b

#방법 1
# print("나는 %d살입니다." %20);
# print("나는 %s을 좋아합니다." %"파이썬");
# print("Apple 은 %c로 시작함" %"A");
#print("나는 %s색과 %s색을 좋아합니다." %("빨간","파란"));

#방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아합니다." .format("빨간","파란"));
# print("나는 {0}색과 {1}색을 좋아합니다." .format("빨간","파란"));
# print("나는 {1}색과 {0}색을 좋아합니다." .format("빨간","파란"));

#방법 3
#print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨강"));
#print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨강",age = 20 ));

#방법 4(v 3.6 이상)

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요".format(color="빨강",age = 20 ))

#탈출문자
# \n: 줄바꿈
# \"문자\" => "문자"
# \\ 문장내에서 \
# \r : 커서를 맨 앞으로 이동
# \b : 백스페이스 (한글자 씩 삭제)
# \t : 탭
print("백문이 불여일견 \n백견이 불여일타")

print("나는 \"이주헌\" 이다")
print("C:\\Users\\")
print("Red Apple\rPine"); # PineApple
print("Redd\bApple"); #RedApple
print("Red\tApple");


#Quiz
#사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
#예) http://naver.com
#규칙 1 : http:// 부분은 제외 => naver.com
#규칙 2 : 처음만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + '!'로 구성
#예 ) 생성된 비밀번호 : nav51!
print("================Quiz================================================")
site = "http://naver.com"
site = site.replace("http://","");
site = site[:site.index(".")];
password = site[0:3] + str(len(site)) + str(site.count("e")) + "!"

print("생성된 패스워드는 {} 입니다.".format(password))
