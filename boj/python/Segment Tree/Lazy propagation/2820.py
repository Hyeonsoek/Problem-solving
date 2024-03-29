import sys
import math
input = sys.stdin.readline

def euler(tree, n):
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
    
    salary = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    salary[1] = int(input())
    for x in range(2, n + 1):
        value, parent = map(int, input().split())
        salary[x] = value
        graph[parent].append(x)
    
    starts, ends = euler(graph, n)
    
    height = math.ceil(math.log2(n))
    size = 1 << (height + 1)
    tree = [0 for _ in range(size)]
    lazy = [0 for _ in range(size)]
    
    def propagate(node, start, end):
        if lazy[node]:
            if start != end:
                lazy[node << 1] += lazy[node]
                lazy[node << 1 | 1] += lazy[node]
            
            tree[node] += (end - start + 1) * lazy[node]
            lazy[node] = 0
    
    def update(left, right, value, node=1, start=1, end=n):
        propagate(node, start, end)
        
        if end < left or right < start:
            return
        
        if left <= start and end <= right:
            lazy[node] += value
            propagate(node, start, end)
            return

        mid = (start + end) >> 1
        update(left, right, value, node << 1, start, mid)
        update(left, right, value, node << 1 | 1, mid + 1, end)
        
        tree[node] = tree[node << 1] + tree[node << 1 | 1]
        
    def query(index, node=1, start=1, end=n):
        propagate(node, start, end)
        
        if start == end:
            return tree[node]
        
        mid = (start + end) >> 1
        if index <= mid:
            return query(index, node << 1, start, mid)
        else:
            return query(index, node << 1 | 1, mid + 1, end)
        
    for x in range(1, n + 1):
        update(starts[x], starts[x], salary[x])
    
    for _ in range(m):
        q, *a = input().strip().split()
        
        if q == 'p':
            index, value = map(int, a)
            if starts[index] > ends[index]:
                continue
            
            update(starts[index] + 1, ends[index], value)
        else:
            index, = map(int, a)
            print(query(starts[index]))
    
solve()