n = input().split(",")
res = []
for i in n:
    if int(i,2) % 5 == 0:
        res.append(i)
print(",".join(res))