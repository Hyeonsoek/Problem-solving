import sys
input = sys.stdin.readline

def damage(time, r, a, d):
    xx, rr = divmod(time, r + a)
    damage = xx * d
    if r <= rr < r + a:
        damage += (rr - r) * d / a
    return damage


def solve():
    n, s, e = map(int, input().split())
    
    result = 0
    for x in range(n):
        R, A, D = map(int, input().split())
        sdamage = damage(s, R, A, D)
        edamage = damage(e, R, A, D)
        result += edamage - sdamage
    
    print(result / (e - s))    

solve()