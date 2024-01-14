from queue import PriorityQueue

n, m = map(int, input().split())

warp = { }
for _ in range(n + m):
    start, end = map(int, input().split())
    warp[start] = end 

check = [ False ] * 101

que = PriorityQueue()
que.put((0, 1))
check[1] = True

while not que.empty():
    cost, start = que.get()
    
    if start == 100:
        print(cost)
        exit(0)
    
    for x in range(1, 7):
        if start + x > 100 or check[start + x]:
            continue
        
        if start + x in warp:
            check[warp[start + x]] = True
            que.put((cost + 1, warp[start + x]))
        else:
            check[start + x] = True
            que.put((cost + 1, start + x))