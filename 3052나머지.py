a = []
for _ in range(1,11):
    n = int(input())
    a.append(n % 42)

print(len(set(a)))