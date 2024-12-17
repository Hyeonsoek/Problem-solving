import heapq
import sys
print = sys.stdout.write

def solve():
    n, m, k = map(int, input().split())
    queue = [-int(input()) for _ in range(n)]
    heapq.heapify(queue)

    value = 0
    result = []
    while queue:
        di = -heapq.heappop(queue)
        
        if di > k:
            heapq.heappush(queue, m - di)
            value = value // 2 + di
            result.append(value)

    print(f'{len(result)}\n')
    for x in result:
        print(f'{x}\n')
        
solve()