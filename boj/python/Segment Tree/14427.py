import sys, math
input = sys.stdin.readline
MAX = 10 ** 9

def init(node, start, end):
    if start == end:
        tree[node] = (array[start], start)
        return tree[node]

    mid = (start + end) >> 1
    LL = init(node << 1, start, mid)
    RR = init((node << 1) + 1, mid + 1, end)
    
    if LL[0] < RR[0]:
        tree[node] = LL
    else:
        if LL[0] == RR[0]:
            if LL[1] < RR[1]:
                tree[node] = LL
            else:
                tree[node] = RR
        else:
            tree[node] = RR
    
    return tree[node]

def update(node, start, end, index, value):
    if index < start or end < index:
        return
    
    if start == end:
        tree[node] = (value, start)
        return
    
    mid = (start + end) >> 1
    update(node << 1, start, mid, index, value)
    update((node << 1) + 1, mid + 1, end, index, value)
    
    LL = tree[node << 1]
    RR = tree[(node << 1) + 1]
    
    if LL[0] < RR[0]:
        tree[node] = LL
    else:
        if LL[0] == RR[0]:
            if LL[1] < RR[1]:
                tree[node] = LL
            else:
                tree[node] = RR
        else:
            tree[node] = RR
    
    
n = int(input())
array = [0] + list(map(int, input().split()))
tree = [ (0, 0) ] * (4 * n)

init(1, 1, n)

m = int(input())
for _ in range(m):
    q = input()
    
    if q[0] == '2':
        print(tree[1][1])
    else:
        q, a, b = map(int, q.split())
        update(1, 1, n, a, b)
        array[a] = b