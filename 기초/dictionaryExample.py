fruit = ["사과","딸기","참외","수박","바나나","사과","딸기","참외"]
d = {}
for f in fruit:
    if f in d:
        d[f] = d[f] + 1
    else:
        d[f] = 1
print(d)