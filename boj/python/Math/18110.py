import sys
input = sys.stdin.readline

def rround(x):
    return int(x) + (1 if x - int(x) >= 0.5 else 0)

n = int(input())
array = sorted([ int(input()) for _ in range(n) ])

cut = rround(n * 0.15)
print( rround(sum(array[cut:n-cut])/(n-2*cut)) if n else 0 )