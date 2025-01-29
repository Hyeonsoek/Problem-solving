import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = list(map(lambda x: int(x) % m, input().split()))
    
    for i in range(1, n):
        arr[i] = (arr[i] + arr[i - 1]) % m
    
    result = 0
    for i in range(n):
        result += arr[i] == 0
    
    print(2 ** result - 1)

solve()