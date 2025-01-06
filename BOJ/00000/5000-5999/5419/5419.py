import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]
    coords.sort(key = lambda x : (x[0], -x[1]))
    
    ycoord = []
    for x in range(n):
        xx, yy = coords[x]
        ycoord.append(yy)
    ycoord.sort()
    
    ycompress = {}
    for x in range(n):
        ycompress[ycoord[x]] = x + 1

    tree = [0] * (n + 1)
    
    def update(x):
        while x <= n:
            tree[x] += 1
            x += x & -x
    
    def query(x):
        result = 0
        while x > 0:
            result += tree[x]
            x -= x & -x
        return result
    
    answer = 0
    for x in range(n):
        xx, yy = coords[x]
        answer += query(n) - query(ycompress[yy] - 1)
        update(ycompress[yy])
    
    print(answer)

for _ in range(int(input())):
    solve()