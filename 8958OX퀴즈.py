n = int(input())

b = []
for _ in range(n):
    count = 0
    result = 0
    a = list(input().upper())

    for i in a:
        if i == 'O':
            count += 1
            result += count
        else:
            count = 0
    b.append(result)
    
for j in range(len(b)):
    print(b[j])

    