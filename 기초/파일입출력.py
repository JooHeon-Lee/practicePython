# score_file = open("score.txt","w",encoding="utf-8") # 이파일을 쓰겠다
# print("수학 : 0", file=score_file)
# print("영어 : 50",file=score_file)
# score_file.close() 파일은 사용후 닫아줘야함

# score_file = open("score.txt","a",encoding="utf-8") # 이미 존재하는파일에 이어쓸때(append)
# score_file.write("과학 : 80") #write사용시 줄바꿈해줘야함
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt","r",encoding="utf-8") # r은 리드
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r",encoding="utf-8")
# print(score_file.readline(),end="") # 한줄만 읽어옴 한줄읽고 커서는 다음줄로 이동
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")

#몇줄인지 모를때
# score_file = open("score.txt","r",encoding="utf-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()

#리스트에 넣어서 처리
score_file = open("score.txt","r",encoding="utf-8")
lines = score_file.readlines()
print(lines)
for line in lines:
    print(line,end="")
score_file.close()