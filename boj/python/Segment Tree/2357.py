import sys, math
input = sys.stdin.readline

MAX = 10 ** 9
MIN = 0

n, m = map(int, input().split())
array = [0] + [ int(input()) for _ in range(n) ]

height = 1 << (int(math.ceil(math.log2(n))) + 1)
tree = [(0, 0) for _ in range(height)]

def init(node, start, end):
    if start == end:
        tree[node] = (array[start], array[start])
        return tree[node]
    else:
        mid = (start + end) // 2
        LL = init(node * 2, start, mid)
        RR = init(node * 2 + 1, mid + 1, end)
        tree[node] = (min(LL[0], RR[0]), max(LL[1], RR[1]))
        return tree[node]
    
def find(node, start, end, left, right):
    if left > end or start > right:
        return (MAX, MIN)
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    LL = find(node * 2, start, mid, left, right)
    RR = find(node * 2 + 1, mid + 1, end, left, right)
    
    return (min(LL[0], RR[0]), max(LL[1], RR[1]))
        
init(1, 1, n)

for _ in range(m):
    a, b = map(int, input().split())
    result = find(1, 1, n, a, b)
    print(*result)