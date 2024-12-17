import sys
input = sys.stdin.readline

n = int(input())
tree = [(0, 0) for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a] = (b, c)
    if b != -1:
        indegree[b] += 1
    if c != -1:
        indegree[c] += 1

index, height = 1, 0
levels = [(n, 0) for _ in range(n)]

def inorder(x, h):
    global index, height
    
    height = max(height, h)
    
    if tree[x][0] != -1:
        inorder(tree[x][0], h + 1)
    
    lmax, lmin = levels[h]
    levels[h] = (min(lmax, index), max(lmin, index))
    index += 1
    
    if tree[x][1] != -1:
        inorder(tree[x][1], h + 1)

for x in range(1, n + 1):
    if indegree[x] == 0:
        inorder(x, 0)

result = [ (xmin - xmax - 1, level + 1) for level, (xmin, xmax) in enumerate(levels[:height+1]) ]
width, level = min(result)

print(level, -width)