from collections import deque

def solve():
    n, k = map(int, input().split())
    queue = deque()
    for x in range(1, n + 1):
        card = [*map(int, input().split())]
        for xx in range(k):
            queue.append((x, card[xx]))
    
    while len(queue) > 1:
        index, count = queue.popleft()
        for x in range(count - 1):
            queue.append(queue.popleft())
            
    return queue.pop()
        
print(*solve())