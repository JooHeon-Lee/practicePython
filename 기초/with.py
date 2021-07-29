# import pickle

# # close필요없음 자동으로 해줌
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬 열공중")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())