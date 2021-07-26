#continue 와 break

absent = [2,5] #결석
no_book = [7] # 책을 깜박했음
for student in range(1,11):# 1~10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로".format(no_book))
        break
    print("{0}, 책을 읽어봐".format(student))