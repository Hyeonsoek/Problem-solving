import sys
from math import *

while True:
    n, m = map(int, sys.stdin.readline().split())
    if (n, m) == (0, 0):
        break
    
    g = gcd(n, m)
    
    if n == g:
        print('factor')
    elif m == g:
        print('multiple')
    else:
        print('neither')