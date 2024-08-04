import sys
from collections import *
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]

    count = defaultdict(int)
    for x in range(n):
        count[arr[x]] += 1

    u, d = map(int, input().split())

    c1, c2, c3 = count[1], count[2], count[3]

    for x in range(c3 + 1):
        k, l = x, c3 - x
        if c1 + k == u and c2 + l == d:
            print('YES')
            break
    else:
        print("NO")
        return

    result = ''
    for x in range(n):
        match arr[x]:
            case 1:
                result += 'U'
            case 2:
                result += 'D'
            case 3:
                result += 'U' if k > 0 else 'D'
                k -= 1

    print(result)

solve()