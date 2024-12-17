from math import gcd

def X123(CL, CR):
    GCD = gcd(CL, CR)
    X1 = CL // GCD
    X3 = CR // GCD
    X2 = CR // X3
    return X1, X2, X3

def solve():
    C = [*map(int, input().split())]
    
    X1, X2, X3 = X123(C[0], C[4])
    X7, X6, X5 = X123(C[2], C[5])
    
    print(X1, X2, X3, X5, X6, X7)

solve()