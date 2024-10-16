import sys
input = sys.stdin.readline

def solve():
    n , k = map(int, input().split())
    arr = [*map(int, input().split())]
    brr = []
    
    for x in range(n):
        brr.append(arr[x] - x * k)
    
    result = 0
    maxvalue = max(brr)
    for x in range(n):
        result += maxvalue - brr[x]
    
    print(result)
    
solve()