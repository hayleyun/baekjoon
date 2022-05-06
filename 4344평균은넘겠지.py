c = int(input())

count = 0
for _ in range(c):
    a = list(map(int,input().split(' ')))
    b = (sum(a) - a[0]) / a[0] # 한 줄 평균
    for i in a[1:]:
        if (i > b):
            result = count / a[0] * 100
            count += 1
    print(f'{result:.3f}%')