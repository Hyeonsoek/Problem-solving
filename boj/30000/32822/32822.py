import sys
input = lambda : map(int, sys.stdin.readline().split())

def solve():
    n, m = input()
    A = [[*input()] for _ in range(n)]
    B = [[*input()] for _ in range(n)]
    M = [*input()]

    SetM = list(set(M))
    diff = [0 for _ in range(n)]    
    for i in range(len(SetM)):
        b = SetM[i] - 1
        for a in range(n):
            diff[b] = max(diff[b], abs(A[a][b] - B[a][b]))
    
    result = 0
    for x in range(m):
        result += diff[M[x] - 1]

    print(result)

solve()