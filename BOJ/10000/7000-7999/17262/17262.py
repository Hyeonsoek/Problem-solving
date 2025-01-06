import sys
input = sys.stdin.readline

n = int(input())
smax, emin = 1, 10 ** 5
for _ in range(n):
    s, e = map(int, input().split())
    smax = max(s, smax)
    emin = min(e, emin)
    
print(max(0, smax - emin))