def solve():
    k = abs(int(input()))

    if not k:
        return 0

    if not k & 1:
        return -1
    
    start = 1
    result = 1
    while start < k:
        start = start * 2 + 1
        result += 1
    
    return result

print(solve())