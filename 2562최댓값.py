n = []
for i in range(1,10):
    n.append(int(input()))
print(max(n))
print(n.index(max(n)) + 1)