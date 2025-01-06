import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n, q, k = map(int, input().split())
    
    last = 0
    query = []
    for x in range(q):
        qq = [*map(int, input().split())]
        query.append(qq)
        
        if qq[0] == 1:
            last = max(last, x)
    
    stack = []
    for x in range(last + 1):
        if query[x][0] == 0:
            stack.append(query[x][1])
    
    stack = deque(sorted(stack))
    
    arrow = 1
    for x in range(last + 1, q):
        if query[x][0] == 0:
            if arrow & 1:
                stack.appendleft(query[x][1])
            else:
                stack.append(query[x][1])
        else:
            arrow ^= 1
    
    if arrow & 1:
        print(stack[k - 1])
    else:
        print(stack[len(stack) - k])
    
solve()