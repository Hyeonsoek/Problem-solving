import sys
input = sys.stdin.readline

def solve():
    s = []
    
    q = int(input())
    for _ in range(q):
        query, *a = map(int, input().split())
        
        if query == 1:
            x, = a
            s.sort(reverse=(x == 2))
        else:
            x, t = a
            s = s[:x] + [t] + s[x:]
    
    print(len(s))
    print(*s)

solve()