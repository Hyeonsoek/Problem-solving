def solve():
    n = int(input())
    real = list(map(int, input().split()))
    m = int(input())
    dream = list(map(int, input().split()))

    depth = m
    while depth * (n - 1) + n > len(dream):
        depth -= 1

    max_res = -1
    min_res = m
    for dep in range(depth, -1, -1):
        count = dep * (n - 1) + n
        for y in range(m - count + 1):
            if dream[y::dep+1][:n] == real:
                min_res = min(min_res, dep)
                max_res = max(max_res, dep)
        
    if max_res != -1:
        print(min_res, max_res)
    else:
        print(-1)
        
solve()