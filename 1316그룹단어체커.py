a = int(input())
b = a
for _ in range(a):
    list = []
    now = ''
    words = input()
    for i in words:
        if i not in list:
            list.append(i)
            now = i
        elif i != now:
            b -= 1
            break
print(b)