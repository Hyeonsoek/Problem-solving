import sys
input = sys.stdin.readline

def solve():
    fn = {str(i) : x for i, x in enumerate(input().split())}
    fr = {fn[str(i)] : str(i) for i in range(10)}
    A, B = map(lambda x: [*x], input().split())
    
    for i in range(len(A)):
        A[i] = fr[A[i]]
    A = int(''.join(A))
    
    for i in range(len(B)):
        B[i] = fr[B[i]]
    B = int(''.join(B))
    
    AB = [*str(A + B)]
    for i in range(len(AB)):
        AB[i] = fn[AB[i]]
    
    print(''.join(AB))

solve()