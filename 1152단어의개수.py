a = list(input().split())

cnt = 0
for i in range(1,len(a)):
    if a[0] == "" or a[-1] == "":
        cnt += 1
        print(len(cnt) -1)
    else:
        cnt += 1
print(len(a))