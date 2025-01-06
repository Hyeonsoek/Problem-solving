import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [[*map(int, input().split())] for _ in range(n)]
    
    result = 1
    s = set(arr[0])
    for x in range(1, n):
        for xx in range(3):
            if arr[x][xx] in s:
                break
        else:
            result += 1
            
        s |= set(arr[x])
    
    print(result)
        
solve()