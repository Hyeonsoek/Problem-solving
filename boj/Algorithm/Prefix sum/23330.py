import sys
input = sys.stdin.readline

def solve(): 
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    prefix = [0]
    for x in range(n):
        prefix.append(prefix[-1] + arr[x])

    result = 0
    for x in range(n):
        plus = prefix[n] - prefix[x] - arr[x] * (n - x)
        minus = abs(prefix[x] - arr[x] * x)
        
        result += plus
        result += minus

    print(result)
    
solve()