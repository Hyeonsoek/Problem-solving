import sys
MAX = 1000001
input = sys.stdin.readline

def solve():
    cache = [1] * MAX
    cache[1] = 0
    for i in range(1, 1001):
        cache[i * i] = 0 
    
    for i in range(1, MAX):
        if cache[i]:
            j = 1
            while i + j * j < MAX:
                cache[i + j * j] = 0
                j += 1
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        print("cubelover" if cache[n] else "koosaga")

solve()