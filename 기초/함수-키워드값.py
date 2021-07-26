def profile(name, age, main_lang): # 기본값 세팅 전달 받지 않았을때
     print(name,age,main_lang)

profile(name="유재석",main_lang="파이썬",age=20)# 키워드 = 값을 넣으면 순서 상관없이 값 매칭됨
profile(main_lang="파이썬",name="김태호",age=25)