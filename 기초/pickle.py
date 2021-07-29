# 프로그램상에서 사용하고있는 데이터를 파일형태로 저장해주는것
# 그 파일을 또 pickle로 가져와서 쓸수있음
import pickle
# profile_file = open("profile.pickle","wb") # 쓰기목적 b 는 바이너리 피클을쓸때는 꼭 써줘야함 인코딩필요 x
# profile = {"이름" : "박명수","나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile 에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle","rb") # 읽기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
