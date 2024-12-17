import sys
import heapq
input = sys.stdin.readline

def solve():
    n, k, x, y = map(int, input().split())
    street = [[] for _ in range(n+1)]
    for _ in range(x):
        start, end, minute = map(int, input().split())
        street[start].append((end, minute))
        street[end].append((start, minute))
    
    road = [[] for _ in range(n+1)]
    for _ in range(y):
        start, end, minute = map(int, input().split())
        road[start].append((end, minute))
        road[end].append((start, minute))
    
    time = [sys.maxsize for _ in range(n + 1)]
    time[1] = 0

    queue = [(0, 1)]
    while queue:
        minute, vertex = heapq.heappop(queue)
        
        if time[vertex] < minute:
            continue
        
        for nbr, nbrtime in street[vertex]:
            nexttime = minute + nbrtime
            if time[nbr] > nexttime:
                time[nbr] = nexttime
                heapq.heappush(queue, (nexttime, nbr))
        
        for nbr, nbrtime in road[vertex]:
            nexttime = max(minute, k) + nbrtime
            if time[nbr] > nexttime:
                time[nbr] = nexttime
                heapq.heappush(queue, (nexttime, nbr))
                    
    print(time[n])

solve()