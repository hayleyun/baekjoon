import string
a = input().upper()
# a = a.upper()
alpha = string.ascii_uppercase

cnt = 0
b = []
for i in alpha:
    if a.count(i) > alpha.count(i):
        cnt = a.count(i)
        b.append(i)
        
        if len(b) > 1:
            print('?')
        else:
            print(",".join(b))