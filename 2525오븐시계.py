H, M =map(int, input().split(' '))
m = int(input())

M = M + m
H = H + (M // 60)
if(M >= 60):
    M = M % 60
if(H >= 24):
    H = abs(24 - H)
    
print(H, M)