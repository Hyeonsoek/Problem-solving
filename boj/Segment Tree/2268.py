import sys
input = sys.stdin.readline

def update(x, value):
    while x <= n:
        tree[x] += value
        x += x & -x

def fsum(x):
    result = 0
    while x > 0:
        result += tree[x]
        x -= x & -x
    return result


n, m = map(int, input().split())
array = [0] * (n + 1)
tree = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    
    if a:
        update(b, c - array[b])
        array[b] = c
    else:
        if b > c:
            print(fsum(b) - fsum(c-1))
        else:
            print(fsum(c) - fsum(b-1))