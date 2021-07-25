#표준 체중을 구하는 프로그램
# 각 개인의 키에 적당한 체중
#(성별에 따른 공식)
# 남자 : 키 x 키 x 22
# 여자 : 키 x 키 x 21

#조건 1 : 표준 체중은 별도의 함수 내에서 계산
#   함수명 : std_weight
#   전달값 : 키(height), 성별(gender)
#조건 2 : 표준 체중은 소주점 둘째자리까지 표시

#출력 예제
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weigth(height,gender): # m 단위
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm단위
gender = "남자"
weight = round(std_weigth(height / 100 ,gender),2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))