import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque(sorted([int(input()) for _ in range(n)]))

result = 0
while len(arr) > 1:
    maxvalue = arr.pop()
    minvalue = arr.popleft()
    
    result += 2 * maxvalue

if arr:
    result += arr.pop()
    
print(result)