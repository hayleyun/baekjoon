import string
a = input().upper()

alpha = string.ascii_uppercase

b = []
max_len=0
for i in alpha:
    if a.count(i)>max_len:# a의 알파벳중 최대빈도수를 미리 기록
        max_len=a.count(i)
        
for i in alpha:
    if a.count(i)==max_len: # a의 알파벳들의 최대빈도수와 같다면
        b.append(i) # b에 해당 알파벳 추가
if len(b) > 1: # 최대빈도수를 가진 알파벳이 2개이상이라면 ? 출력
    print('?')
else:
    print(",".join(b))