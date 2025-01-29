from collections import *

def solve():
    n = int(input())
    q = deque(range(1, n + 1))
    
    while q:
        print(q.popleft(), end=' ')
        if q:
            q.append(q.popleft())

solve()