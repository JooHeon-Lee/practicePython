print("Python" , "Java" , sep=",",end="?") # seperator ""사이에 들어감
print("무엇이 더 재밌을까요?")# end 명시하면 줄바꿈을하지않고 해당문자나옴

import sys
print("Python","Java",file=sys.stdout) ## 표준 출력
print("Python","Java",file=sys.stderr) ## 표준 에러로 처리(에러확인시)

#출력포맷

#시험성적
scores = {"수학":0, "영어" :50,"코딩":100}

for subject,scores in scores.items():
   # print(subject,scores)
   print(subject.ljust(8),str(scores).rjust(4),sep=":") #ljust는 왼쪽으로 정력 8자리 공간을 확보
                                                #scores는 오른쪽정렬을하는데 4칸을 확보함
#은행 대기순번표
# 001 002 003 ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) #zfill은 0으로 채움 인수는 크기 값이없으면 0으로

#표준 입력
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")