import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    p1, p2 = map(int, input().split())
    m = int(input())
    s = int(input())
    
    dm1 = abs(p1 - m)
    dm2 = abs(p2 - m)
    sm1 = abs(p1 - s)
    sm2 = abs(p2 - s)
    ms = abs(m - s)

    isP1 = bool(dm1 & 1)
    isP2 = bool(dm2 & 1)

    if not isP1 and not isP2:
        return -1

    if m < p1 < p2:
        if s <= p1 < p2:
            if isP1:
                return dm1 + ms
            if isP2:
                if s == 1 or m == 1:
                    return -1
                if s <= m:
                    return dm2 + ms + sm1 + 1
                return dm2 + ms + dm1 + 1

        elif p1 < s < p2:
            if isP1:
                return dm1 + ms
            if isP2:
                if m == 1:
                    return -1
                return dm2 + ms + dm1 + 1
            
        else:
            if isP1:
                if s == n:
                    return -1
                return dm1 + ms + sm2 + 1
            if isP2:
                if m == 1:
                    return -1
                return dm2 + ms + dm1 + 1

    elif p1 < m < p2:
        if s <= p1 < p2:
            if isP1 and isP2:
                if dm1 < dm2:
                    return dm1 + ms
                else:
                    if s == 1:
                        return dm1 + ms
                    return min(dm1 + ms, dm2 + ms + sm1 + 1)
                
            if isP1 and not isP2:
                return dm1 + ms
            
            if not isP1 and isP2:
                if s == 1:
                    return -1
                return dm2 + ms + sm1 + 1

        elif p1 < s < p2:
            if isP1 and isP2:
                if dm1 < dm2:
                    return dm1 + ms
                else:
                    return dm2 + ms

            if isP1 and not isP2:
                return dm1 + ms

            if not isP1 and isP2:
                return dm2 + ms

        else:
            if isP1 and isP2:
                if dm1 < dm2:
                    if s == n:
                        return dm2 + ms
                    return min(dm1 + ms + sm2 + 1, dm2 + ms)
                else:
                    return dm2 + ms

            elif isP1 and not isP2:
                if s == n:
                    return -1
                return dm1 + ms + sm2 + 1

            elif not isP1 and isP2:
                return dm2 + ms

    elif p1 < p2 < m:
        if s <= p1 < p2:
            if isP2:
                if s == 1:
                    return -1
                return dm2 + ms + sm1 + 1

            if isP1:
                if m == n:
                    return -1
                return dm1 + ms + dm2 + 1

        elif p1 < s < p2:
            if isP2:
                return dm2 + ms
            if isP1:
                if m == n:
                    return -1
                return dm2 + ms + dm1 + 1

        else:
            if isP2:
                return dm2 + ms
            if isP1:
                if s == n or m == n:
                    return -1
                if m <= s:
                    return dm1 + ms + sm2 + 1
                return dm1 + ms + dm2 + 1

    return -1

print(solve())