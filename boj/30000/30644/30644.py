import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    index = {}
    
    for i, x in enumerate(sorted(arr)):
        index[x] = i
        
    result = 0
    for x in range(1, n):
        if abs(index[arr[x]] - index[arr[x-1]]) != 1:
            result += 1
            
    print(result)
    
solve()