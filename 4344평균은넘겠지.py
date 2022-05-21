c = int(input())
d = []
for _ in range(c):
    count = 0
    a = list(map(int,input().split()))
    b = (sum(a) - a[0]) / a[0] # 한 줄 평균
    for i in a[1:]:
        if (i > b):
            count += 1
            result = count / a[0] * 100
        else:
            result = count /a[0] * 100
    d.append(result)

for j in range(len(d)):
    print(f'{d[j]:.3f}%')