import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    
    queue = deque()
    for i in range(n):
        if not a[i]:
            queue.append(b[i])
    
    result = []
    m = int(input())
    c = [*map(int, input().split())]
    for i in range(m):
        queue.appendleft(c[i])
        result.append(queue.pop())
    
    print(*result)
    
solve()