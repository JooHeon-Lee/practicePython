# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1}\t주 사용 언어 : {2}".format(\
#         name,age,main_lang))

# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")

# 같은 학교 같은 학년 같은 반 같은 수업을 들을때 
# 나이랑 언어는 같음 
# 프로필을 만들때마다 넣기 번거로움 그때 기본값 사용

def profile(name, age=17, main_lang="파이썬"): # 기본값 세팅 전달 받지 않았을때
     print("이름 : {0}\t 나이 : {1}\t주 사용 언어 : {2}".format(\
         name,age,main_lang))

profile("유재석",25)
profile("김태호")