import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = [*map(int, input().split())]
    tree = [0] * (n + m + 1)

    def update(x, value):
        while x <= n + m:
            tree[x] += value
            x += x & -x
    
    def query(x):
        result = 0
        while x > 0:
            result += tree[x]
            x -= x & -x
        return result
        
    index = {x: x + m for x in range(1, n + 1)}
    
    for x in range(1, n + 1):
        update(x + m, 1)
    
    answer = []
    for x in range(m):
        k = index[arr[x]]
        answer.append(query(k - 1))
        update(k, -1)
        update(m - x, 1)
        index[arr[x]] = m - x
    
    print(*answer)

for _ in range(int(input())):
    solve()