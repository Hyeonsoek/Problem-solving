from collections import deque

def solve():
    n = int(input())
    t = int(input())
    queue = deque(map(int, input().split()))
    
    result = []
    for i in map(int, input().split()):
        i -= 1
        while i > 0:
            queue.append(queue.popleft())
            i -= 1
        result.append(queue[0])
    
    print(*result)

solve()