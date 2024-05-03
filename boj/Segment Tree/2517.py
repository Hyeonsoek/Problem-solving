import sys
input = sys.stdin.readline

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

n = int(input())
array = sorted([(int(input()), x + 1) for x in range(n)], reverse=True)
tree = [0] * (n + 1)

result = [0] * (n + 1)
for _, x in array:
    result[x] = query(x) + 1
    update(x)

for x in range(1, n + 1):
    print(result[x])