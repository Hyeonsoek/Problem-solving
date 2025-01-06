def solve():
    n, m = map(int, input().split())
    products = [([*map(int, input().split())][1:], x+1) for x in range(n)]
    products.sort(key=lambda x : len(x[0]), reverse=True)
    
    order = []
    visited = [0] * (m + 1)
    for items, i in products:
        order.append(i)
        for x in items:
            if visited[x]:
                continue
            visited[x] = i

    for x in range(1, m + 1):
        if visited[x] == 0:
            print("NO")
            return

    print("YES")
    print(*order[::-1])
    print(*visited[1:])

solve()