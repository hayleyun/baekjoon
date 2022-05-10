def self_num():
    n = list(range(1,10001))
    for i in range(10001):
        a = str(i)
        if len(a) == 1:
            b = int(a)
            result = b + b
        if len(a) == 2:
            result = int(a) + int(a[0]) + int(a[1])
        if len(a) == 3:
            result = int(a) + int(a[0]) + int(a[1]) + int(a[2])
        if len(a) == 4:
            result = int(a) + int(a[0]) + int(a[1]) + int(a[2]) + int(a[3])
        if len(a) == 5:
            result = int(a) + int(a[0]) + int(a[1]) + int(a[2]) + int(a[3]) + int(a[4])
        if result in n:
            n.remove(result)
    for i in n:
        print(i)

self_num()
