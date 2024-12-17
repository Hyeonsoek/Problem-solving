MAX = 100000

def solve():
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    k = int(input())
    
    cache = [MAX] * MAX
    
    for value in arr:
        cache[value] = 1
    
    for value in range(2, MAX):
        for x in range(n):
            if value >= arr[x]:
                cache[value] = min(cache[value], cache[value - arr[x]] + 1)
    
    for x in range(1, MAX):
        if cache[x] > k:
            return f"{'jjaksoon' if x & 1 else 'holsoon'} win at {x}"

print(solve())