import sys
sys.setrecursionlimit(600001)
MAX = 300001
input = sys.stdin.readline

class Node:
    def __init__(self) -> None:
        self.start = 0
        self.end = 0
        self.children = []
        
def set_range(tree, node, value):
    tree[node].start = value
    for child in tree[node].children:
        value = set_range(tree, child, value + 1)
    tree[node].end = value
    return value

def make_tree(n):
    tree = [Node() for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for x in range(1, n + 1):
        c, *children = map(int, input().split())
        for child in children:
            indegree[child] += 1
            tree[x].children.append(child)
    
    for x in range(1, n + 1):
        if not indegree[x]:
            return tree, x

def solve() -> int:
    n, m, k, s = map(int, input().split())
    tree, start = make_tree(n)
    tree_mod, start_mod = make_tree(n + s)
    
    if s > k:
        return 0
    
    for x in tree_mod:
        if len(x.children) > m:
            return 0
    
    set_range(tree_mod, start_mod, 1)
    
    def dfs(start):
        result = True
        node = tree_mod[start]
        
        for child in tree[start].children:
            c = tree_mod[child]
            result &= node.start <= c.start <= node.end
            result &= dfs(child)
            
        return result

    return 1 if dfs(start) else 0
        
    
print(solve())