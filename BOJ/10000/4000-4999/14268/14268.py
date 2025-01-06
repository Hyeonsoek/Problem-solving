import sys
input = sys.stdin.readline

def eular(tree, n):
    index = 0
    stack = [1]
    start = [0] * (n + 1)
    end = [0] * (n + 1)
    
    while stack:
        node = stack[-1]
        
        if not start[node]:
            index += 1
            start[node] = index
            
            for next in tree[node]:
                stack.append(next)
        else:
            end[node] = index
            stack.pop()
    
    return start, end

def solve():
    n, m = map(int, input().split())
    arr = [*map(int, input().split())]
    graph = [[] for _ in range(n + 1)]
    for x in range(1, n):
        graph[arr[x]].append(x+1)
    
    start, end = eular(graph, n)
    
    tree = [0] * 4 * n
    lazy = [0] * 4 * n
    
    def propagate(node, start, end):
        if lazy[node] != 0:
            if start != end:
                lazy[node << 1] += lazy[node]
                lazy[node << 1 | 1] += lazy[node]
            tree[node] += lazy[node] * (end - start + 1)
            lazy[node] = 0
    
    def update(left, right, value, node = 1, start = 1, end = n):
        propagate(node, start, end)
        
        if end < left or right < start:
            return tree[node]

        if left <= start and end <= right:
            lazy[node] += value
            propagate(node, start, end)
            return tree[node]
        
        mid = (start + end) >> 1
        LL = update(left, right, value, node << 1, start, mid)
        RR = update(left, right, value, node << 1 | 1, mid + 1, end)
        tree[node] = LL + RR
        return tree[node]
    
    def query(index, node=1, start=1, end=n):
        propagate(node, start, end)
        if start == end:
            return tree[node]
        
        mid = (start + end) >> 1
        if index <= mid:
            return query(index, node << 1, start, mid)
        return query(index, node << 1 | 1, mid + 1, end)

    for _ in range(m):
        q, *values = map(int, input().split())
        
        if q == 1:
            i, w = values
            update(start[i], end[i], w)
        else:
            i = values[0]
            print(query(start[i]))
                
solve()