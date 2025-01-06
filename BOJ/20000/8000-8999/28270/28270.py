import sys
sys.setrecursionlimit(1000100)
input = sys.stdin.readline

def solve():
    c = int(input())
    arr = [0, *map(int, input().split())]
    
    tree = [[] for _ in range(c + 1)]
    stack = [[] for _ in range(c + 1)]
    stack[0].append(0)
    
    count = 0
    for x in range(1, c + 1):
        if arr[x] > c:
            print(-1)
            return
        if stack[arr[x] - 1]:
            parent = stack[arr[x] - 1][-1]
            stack[arr[x]].append(x)
            tree[parent].append(x)
            count += 1
    
    if count < c:
        print(-1)
        return
    
    result = []
    def dfs(node):
        for x in range(len(tree[node])):
            result.append(x + 1)
            dfs(tree[node][x])
    
    dfs(0)
    print(*result)

solve()