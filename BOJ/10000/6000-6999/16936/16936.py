import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    
    brr = []
    for i in range(n):
        value = arr[i]
        a = 0
        while value % 2 == 0:
            value //= 2
            a += 1
        
        b = 0
        while value % 3 == 0:
            value //= 3
            b += 1

        brr.append((a, b, arr[i]))

    brr.sort(key = lambda x : (x[0], -x[1]))    
    print(*map(lambda x : x[2], brr))
    
solve()