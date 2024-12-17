from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
gates = [ int(input()) for _ in range(n) ]

low, high = 1, 10 ** 18 + 1
while low <= high:
    mid = (low + high) // 2
    count = sum(map(lambda x : mid // x, gates))
    
    if count < m:
        low = mid + 1
    else:
        high = mid - 1
        
print(low)