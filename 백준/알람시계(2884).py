a,b = map(int,input().split())
if a != 0 and b-45 >= 0:
    print(str(a) + " " + str(b-45))
elif a == 0 and b-45 >= 0:
    print(str(a) + " " + str(b-45))
elif a != 0 and b-45 < 0:
    print(str(a-1) + " " + str(b-45+60))
elif a == 0 and b - 45 < 0:
    a = 24
    print(str(a-1) + " " + str(b-45+60))