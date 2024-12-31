import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr = [ (arr[x], x + 1) for x in range(n) ]
    
    qn = int(input())
    for _ in range(qn):
        L, R = map(int, input().split())
        result = sorted(arr)
        result = result[:L-1] + sorted(result[L-1:R], key=lambda x: x[1]) + result[R:]
        for x in range(n):
            result[x] = (x + 1, result[x][1])
        result.sort(key=lambda x: x[1])
        
        print(*list(zip(*result))[0])
        
solve()