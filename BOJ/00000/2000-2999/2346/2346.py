from collections import deque

def solve():
    n = int(input())
    queue = deque((i, v) for i, v in enumerate(map(int, input().split()), 1))
    
    result = []
    while queue:
        i, v = queue.popleft()
        result.append(i)
        queue.rotate(-v+(v>0))

    print(*result)

solve()