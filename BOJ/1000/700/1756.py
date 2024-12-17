import sys
input = sys.stdin.readline

def solve():
    d, n = map(int, input().split())
    oven = list(map(int, input().split())) # d
    dough = list(map(int, input().split())) # n
    
    for x in range(1, d):
        oven[x] = min(oven[x], oven[x-1])
    
    count = 0
    for x in reversed(range(d)):
        if dough[count] > oven[x]:
            continue
        
        count += 1
        if count >= n:
            return x + 1
    
    return 0
    
print(solve())