from collections import *

def solve():
    n = int(input())
    arr = deque()
    
    for i in reversed(range(1, n + 1)):
        arr.appendleft(i)
        arr.rotate(i)
    
    print(*arr)

solve()