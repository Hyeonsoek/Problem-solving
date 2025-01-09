def solve():
    n, a, b = map(int, input().split())
    for _ in range(8 - n):
        ac, bc = map(int, input().split())
        bc = min(6 - ac, bc)
        a += ac * 3
        b += (ac + bc) * 3
    
    for _ in range(n + 2):
        input()
    
    return "Nice" if a >= 66 and b >= 130 else "Nae ga wae"

print(solve())