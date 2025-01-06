import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    row = []
    column = []
    for _ in range(n):
        r, c = map(int, input().split())
        row.append(r)
        column.append(c)
    row.sort()
    column.sort()
    
    result = 0
    for x in range(n):
        result += abs(row[x] - (x + 1))
        result += abs(column[x] - (x + 1))
    
    print(result)
    
solve()