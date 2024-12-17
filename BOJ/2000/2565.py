import sys
from bisect import *
input = sys.stdin.readline

n = int(input())
arr = []
for x in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()

seq = []
for x in range(n):
    value = arr[x][1]
    if not seq or seq[-1] < value:
        seq.append(value)
    else:
        seq[bisect_left(seq, value)] = value
        
print(n - len(seq))