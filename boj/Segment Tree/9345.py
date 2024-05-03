import sys
from math import ceil, log2
input = sys.stdin.readline

def init(tree, array, node, start, end):
    if start == end:
        tree[node] = (array[start], array[start])
        return tree[node]

    mid = (start + end) // 2
    LL = init(tree, array, node * 2, start, mid)
    RR = init(tree, array, node * 2 + 1, mid + 1, end)
    tree[node] = (min(LL[0], RR[0]), max(LL[1], RR[1]))
    return tree[node]

def query(tree, node, start, end, left, right):
    if right < start or left > end:
        return (100000, 0)
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = query(tree, node * 2, start, mid, left, right)
    RR = query(tree, node * 2 + 1, mid + 1, end, left, right)
    return (min(LL[0], RR[0]), max(LL[1], RR[1]))

def update(tree, node, start, end, index, value):
    if index < start or end < index:
        return tree[node]

    if start == end:
        tree[node] = (value, value)
        return tree[node]

    mid = (start + end) // 2
    LL = update(tree, node * 2, start, mid, index, value)
    RR = update(tree, node * 2 + 1, mid + 1, end, index, value)
    tree[node] = (min(LL[0], RR[0]), max(LL[1], RR[1]))
    return tree[node]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = [x for x in range(n)]
    tree = [(100000, 0) for _ in range((1 << (ceil(log2(n)) + 1)))]
    
    init(tree, array, 1, 0, n - 1)
    
    for _ in range(m):
        q, a, b = map(int, input().split())
        
        if q & 1:
            aa, bb = query(tree, 1, 0, n - 1, a, b)
            print("YES" if aa == a and bb == b else "NO")
        else:
            update(tree, 1, 0, n - 1, array[a], b)
            update(tree, 1, 0, n - 1, array[b], a)
            
            array[a], array[b] = array[b], array[a]
            
#YES NO 때문에 10번 넘게 틀림 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ