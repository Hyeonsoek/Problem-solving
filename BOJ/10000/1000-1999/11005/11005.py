from string import *
t = '0123456789' + ascii_uppercase
n, b = map(int, input().split())
r=''
while n != 0:
    r += t[n % b]
    n //= b
print(r[::-1])