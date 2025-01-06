import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    S = [*map(int, input().split())][::-1]
    E = []
    
    index = 1
    while S or E:
        if S and E:
            s = S[-1]
            e = E[-1]
            if index in [s, e]:
                if index == s:
                    S.pop()
                else:
                    E.pop()
                index += 1
            else:
                E.append(S.pop())
        elif S and not E:
            s = S.pop()
            if index == s:
                index += 1
            else:
                E.append(s)
        elif not S and E:
            e = E.pop()
            if index == e:
                index += 1

    return 'Sad' if index != n + 1 else 'Nice'

print(solve())