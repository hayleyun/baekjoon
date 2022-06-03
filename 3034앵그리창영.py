import math

n, w, h = list(map(int, input().split()))
c = math.sqrt(w**2 + h**2)

for _ in range(n):
    b = int(input())

    if b <= c or b <= w or b <= h:
        print('DA')
    else:
        print('NE')