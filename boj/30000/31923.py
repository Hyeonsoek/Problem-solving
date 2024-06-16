def solve():
    n, p, q = map(int, input().split())
    sb = list(map(int, input().split()))
    sm = list(map(int, input().split()))

    result = []
    for b, m in zip(sb, sm):
        count = 0
        while b != m and count < 10000:
            b += p; m += q
            count += 1
        
        if count < 10000:
            result.append(count)
        else:
            print("NO")
            return
    
    print("YES")
    print(*result)
        
solve()