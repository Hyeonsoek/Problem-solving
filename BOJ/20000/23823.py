import sys
input = sys.stdin.readline
print = sys.stdout.write

def solve():
    n, q = map(int, input().split())

    rows = [0] * (n + 1)
    column = [0] * (n + 1)

    maxr, maxrcount = 0, 0
    maxc, maxccount = 0, 0
    for _ in range(q):
        t, a = map(int, input().split())
        
        match t:
            case 1:
                rows[a] += 1
                if rows[a] > maxr:
                    maxr = rows[a]
                    maxrcount = 1
                elif rows[a] == maxr:
                    maxrcount += 1
            case 2:
                column[a] += 1
                if column[a] > maxc:
                    maxc = column[a]
                    maxccount = 1
                elif column[a] == maxc:
                    maxccount += 1
        
        if not maxrcount:
            print(f'{maxccount * n}\n')
        elif not maxccount:
            print(f'{maxrcount * n}\n')
        else:
            print(f'{maxrcount * maxccount}\n')

solve()