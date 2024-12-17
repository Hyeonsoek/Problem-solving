import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    
    for x in range(n):
        if arr[x]:
            continue
        
        count = 1
        s = set([arr[x]])
        
        if x > 0:
            count += 1
            s.add(arr[x-1])
            
        if x < n - 1:
            count += 1
            s.add(arr[x+1])
        
        for xx in range(1, 4):
            if xx not in s:
                arr[x] = xx
                break
    
    for x in range(1, n):
        if arr[x] == arr[x-1]:
            print(-1)
            return
    
    print(*arr)

solve()