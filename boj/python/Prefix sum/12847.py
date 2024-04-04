def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    prefix = [0]
    for x in range(n):
        prefix.append(prefix[-1] + arr[x])

    result = 0
    for x in range(m, n):
        result = max(result, prefix[x] - prefix[x-m])
        
    print(result)

solve()