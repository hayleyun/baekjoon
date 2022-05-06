a, x = map(int,input().split(' '))
n = list(map(int,input().split(' ')))

for i in range(a):
    if(n[i] < x):
        print(n[i], end=' ')