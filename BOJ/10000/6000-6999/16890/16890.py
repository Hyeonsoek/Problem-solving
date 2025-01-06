from collections import deque

def solve():
    F = sorted([*input()])
    E = sorted([*input()], reverse=True)
    n = len(F)
    
    nn = int(n / 2)
    nnh = int(n / 2 + .5)
    F = deque(F[:nnh])
    E = deque(E[:nn])
    
    L, R = 0, n - 1
    result = [''] * n
    for x in range(n):
        if E and not F:
            result[L] = E.pop()
            continue
        
        if F and not E:
            result[L] = F.pop()
            continue
        
        X = F[0]
        Y = E[0]
        
        if x & 1:
            if X < Y:
                result[L] = E.popleft()
                L += 1
            else:
                result[R] = E.pop()
                R -= 1
        else:
            if X < Y:
                result[L] = F.popleft()
                L += 1
            else:
                result[R] = F.pop()
                R -= 1
    
    print(''.join(result))

solve()