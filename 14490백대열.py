# 유클리드 호제법
n, m = map(int, input().split(':'))

# 쉽게 말하면 큰수에서 작은 수의 나머지값을 주어진 값에 나눈다
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

t = gcd(max(n, m), min(n, m))
print(f'{n // t}:{m // t}')
