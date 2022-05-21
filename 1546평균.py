all = int(input())
n = list(map(int, input().split()))

b = (sum(n) / max(n) * 100) / all
print(b)
