import sys, math
from collections import *
input = sys.stdin.readline

def solve():
    n = int(input())
    m = n * n
    M = sorted([*map(int, input().split())])
    
    A = math.sqrt(M[0])
    if not A.is_integer():
        print('NO')
        return
    A = int(A)
    
    counter = defaultdict(int)
    for i in range(1, m):
        counter[M[i]] += 1
    
    arr = [A]
    for i in range(1, m):
        if counter[M[i]]:
            if M[i] % A:
                print("NO")
                return

            s = M[i] // A
            for v in arr:
                nv = v * s
                for _ in range(2):
                    if not counter[nv]:
                        print("NO")
                        return
                    counter[nv] -= 1

            if not counter[s * s]:
                print("NO")
                return
            
            counter[s * s] -= 1
            arr.append(s)

    print("YES")
    print(*arr)
    
solve()