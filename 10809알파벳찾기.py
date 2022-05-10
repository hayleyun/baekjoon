import string
s = input()

alphabet = string.ascii_lowercase

for i in alphabet:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')

