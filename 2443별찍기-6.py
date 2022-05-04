n = int(input())

for i in range(n+1):
    print(' ' * (i) + '*' * (n-i) + '*' *(n-i-1))