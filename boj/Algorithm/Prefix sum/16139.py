import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    dicts = [[0] * 26]

    for x in s:
        prev = dicts[-1][:]
        prev[ord(x)-97] += 1
        dicts.append(prev)

    q = int(input())
    for x in range(q):
        alpha, l, r = input().split()
        l, r = int(l), int(r)
        alpha = ord(alpha) - 97
        print(dicts[r+1][alpha] - dicts[l][alpha])

solve()