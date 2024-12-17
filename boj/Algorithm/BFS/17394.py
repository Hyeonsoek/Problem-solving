import sys
from collections import deque
MAX = 10**6+1
input = sys.stdin.readline

isPrime = [True] * MAX
isPrime[0] = isPrime[1] = False
for x in range(2, MAX):
    if isPrime[x]:
        for y in range(2*x, MAX, x):
            isPrime[y] = False

def solve():    
    visited = [0] * MAX
    n, a, b = map(int, input().split())
    
    if not sum(isPrime[a:b+1]):
        return -1
    
    queue = deque([(n, 0)])
    while queue:
        curr, count = queue.popleft()
        
        if a <= curr <= b and isPrime[curr]:
            return count
        
        for x in [curr + 1, curr - 1, curr // 3, curr // 2]:
            if 0 <= x < MAX and not visited[x]:
                visited[x] = 1
                queue.append((x, count + 1))
    
    return -1

t = int(input())
for _ in range(t):
    print(solve())