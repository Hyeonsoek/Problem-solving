N, L, I = map(int, input().split())

cache = [[-1] * (N + 1) for _ in range(N + 1)]

def dynamic(n, r):
    if cache[n][r] != -1:
        return cache[n][r]
    
    if n == 0 or r == 0:
        cache[n][r] = 1
        return 1
    
    result = dynamic(n - 1, r)
    if r > 0:
        result += dynamic(n - 1, r - 1)
    cache[n][r] = result
    return result

def find(n, r, k):
    if n == 0:
        return ""
    
    if r == 0:
        return "0" * n
    
    pivot = dynamic(n - 1, r)
    if k <= pivot:
        return "0" + find(n-1, r, k)
    else:
        return "1" + find(n-1, r-1, k-pivot)

print(find(N, L, I))