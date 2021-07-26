# def profile(name, age, lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") # end사용시 줄바꿈 안함
#     print(lang1,lang2,lang3,lang4,lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ") # end사용시 줄바꿈 안함
    for lang in language:
        print(lang, end= " ")
    print()

profile("유재석",20,"Python","Java","C","C++","C#","JavaScript")
profile("김태호",25,"Kotlin","Swift") # 이렇게 빈값넣기 번거로워서 가변인자 사용해야함