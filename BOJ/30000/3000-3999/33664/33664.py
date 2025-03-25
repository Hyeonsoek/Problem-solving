import sys
input = sys.stdin.readline

def solve():
    b, n, m = map(int, input().split())
    items = {}
    for _ in range(n):
        name, price = input().split()
        items[name] = int(price)
    
    total = 0
    for _ in range(m):
        total += items[input().strip()]
    
    if total <= b:
        return "acceptable"
    return "unacceptable"
    
print(solve())