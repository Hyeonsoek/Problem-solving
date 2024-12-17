MAX = 10 ** 9

def solve():
    x, y = map(int, input().split())
    rate = 100 * y // x
    
    low, high = 1, MAX
    while low <= high:
        mid = (low + high) // 2
        current = 100 * (y + mid) // (x + mid)
        
        if rate == current:
            low = mid + 1
        else:
            high = mid - 1

    return -1 if low > MAX else low

print(solve())