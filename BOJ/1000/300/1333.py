def solve():
    n, l, d = map(int, input().split())

    count = 0
    cur = 0
    end = l
    while not end <= cur < end + 5 and count < n:
        if cur < end:
            cur += d
        else:
            end += l + 5
            count += 1
    
    return cur

print(solve())