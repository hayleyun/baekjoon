a, b, c = sorted(map(int, input().split(' ')))
f = [a, b, c]
if(a == b == c):
    print(10000 + a * 1000)
elif(a == b or a == c):
    print(1000 + a  * 100)
else:
    print(max(f) * 100)