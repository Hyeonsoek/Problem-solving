import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    score = [[] for _ in range(4)]
    
    for _ in range(n):
        x, *arr = map(int, input().split())
        for i in range(4):
            score[i].append((arr[i], x))
    
    result = []
    for x in range(4):
        score[x].sort(key=lambda x: (x[0], -x[1]))
        while score[x]:
            value, index = score[x].pop()
            if index not in result:
                result.append(index)
                break
    
    print(*result)

solve()