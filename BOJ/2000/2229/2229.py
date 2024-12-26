import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    cache = [0] * (n + 1)
    
    for i in range(n):
        minvalue = arr[i]
        maxvalue = arr[i]
        for j in reversed(range(i+1)):
            minvalue = min(minvalue, arr[j])
            maxvalue = max(maxvalue, arr[j])
            cache[i + 1] = max(cache[i + 1], cache[j] + maxvalue - minvalue)
    
    print(cache[n])

solve()