n = int(input())

if n < 10:
    a = '0' + str(n)
else:
    a = str(n)

c = a
e = 0
while True:
    b = int(c[0]) + int(c[1])
    b = str(b)
    b = b[-1]
    c = str(c[1]) + b
    e += 1
    if c == a:
        print(e)
        break