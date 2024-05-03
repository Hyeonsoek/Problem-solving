import math
import sys

def lcm(a, b):
    return a * b // math.gcd(a, b)

def henry(a, b):
    x = 0

    while a > 1:
        x = math.ceil(b/a)
        l = lcm(b, x)
        a = a * (l // b) - (l // x)
        b = l

        g = math.gcd(a, b)
        a //= g
        b //= g

    return b


for _ in range(int(input())):
    ai, bi = map(int, sys.stdin.readline().split())
    print(henry(ai, bi))