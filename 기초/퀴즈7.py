# - x주차 주간보고
# 부서 :
# 이름 :
# 엄무 요약 :

#1~50주차까지 보고서 파일 만드는 프로그램
#조건 : 파일명 1주차.txt 2주차.txt

import pickle
for i in range(1,3):
    with open("{0}주차.txt".format(i),"w",encoding="utf8") as study_file:
        study_file.write("부서 : 개발팀")
        study_file.write("이름 : 이주헌")
        study_file.write("업무 요약 : 파이썬 개발")
