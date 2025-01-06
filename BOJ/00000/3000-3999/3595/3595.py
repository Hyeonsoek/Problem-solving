import sys

def solve():
    n = int(input())
    nn = int(n ** .5 + 0.5)
    
    result = sys.maxsize
    abc = (0, 0, 0)
    for a in range(1, nn + 1):
        if n % a == 0:
            for b in range(1, nn + 1):
                if (n // a) % b == 0:
                    c = n // a // b
                    A = 2 * (a * b + b * c + c * a)
                    if result > A:
                        result = A
                        abc = (a, b, c)
    
    print(*abc)

solve()

# abc = n
# 2(ab + bc + ac)