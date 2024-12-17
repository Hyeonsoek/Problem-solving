import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    brr = [*map(int, input().split())]
    
    prev = brr[0]
    arr = [brr[0]]
    for x in range(1, n):
        avg = prev / x
        lower = brr[x]
        upper = brr[x] + 1
        
        if brr[x] == (lower - (lower < avg)):
            prev += lower
            arr.append(lower)
        elif brr[x] == (upper - (upper < avg)):
            prev += upper
            arr.append(upper)
        else:
            print(-1)
            return
    
    if 0 in arr:
        print(-1)
        return
    
    print(*arr)

solve()