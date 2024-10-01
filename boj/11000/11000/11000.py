import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    data = []
    for x in range(n):
        start, end = map(int, input().split())
        data.append((start, 1))
        data.append((end, -1))
    data.sort()

    prefix = [0] * 2 * n
    for x in range(2 * n):
        pos, value = data[x]
        prefix[x] += value
    
    for x in range(1, 2 * n):
        prefix[x] += prefix[x - 1]
    
    print(max(prefix))

solve()