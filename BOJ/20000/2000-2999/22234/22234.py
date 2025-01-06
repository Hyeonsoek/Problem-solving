import sys
from collections import deque, defaultdict
input = sys.stdin.readline
inputmap = lambda: map(int, input().split())

def solve():
    n, t, w = inputmap()
    queue = deque()
    for _ in range(n):
        Px, tx = inputmap()
        queue.append((0, Px, tx))
    
    m = int(input())
    later = defaultdict(tuple)
    for _ in range(m):
        Px, tx, cx = inputmap()
        later[cx] = (Px, tx)
    
    nqueue = deque()
    for x in range(w):
        if x in later:
            queue.append((0, *later[x]))
            
        while nqueue:
            queue.append(nqueue.popleft())
        
        stack, Px, tx = queue.popleft()
        print(Px)
        if tx > 1:
            if stack == t - 1:
                nqueue.append((0, Px, tx - 1))
            else:
                queue.appendleft((stack + 1, Px, tx - 1))

solve()