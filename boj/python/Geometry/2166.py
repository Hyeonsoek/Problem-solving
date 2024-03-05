import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]

    result = 0
    for x in range(n):
        result += coords[x][0] * (coords[(x+1)%n][1] - coords[(x-1)%n][1])

    print(abs(result) * 0.5)

solve()