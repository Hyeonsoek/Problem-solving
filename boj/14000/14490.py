import math

n, m = map(int, input().split(':'))
gcd = math.gcd(n, m)
print(f'{n//gcd}:{m//gcd}')