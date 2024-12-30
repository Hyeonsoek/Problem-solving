import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    indegree = [0] * (n + 1)
    for i, x in enumerate(map(int, input().split()), 1):
        if i != x:
            indegree[x] += 1
    
    count = 0
    for i in range(1, n + 1):
        if indegree[i] == 0:
            count += 1
    
    print(count)

solve()