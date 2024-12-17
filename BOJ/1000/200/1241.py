import sys
MAX = 1000000
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [ int(input()) for _ in range(n) ]

    count = [0] * (MAX + 1)
    for x in range(n):
        count[arr[x]] += 1
        
    for x in range(n):
        result = 0
        for xx in range(1, int(arr[x] ** .5) + 1):
            if arr[x] % xx == 0:
                if xx != arr[x] // xx:
                    result += count[xx] + count[arr[x] // xx]
                else:
                    result += count[xx]
        print(result - 1)
        
solve()