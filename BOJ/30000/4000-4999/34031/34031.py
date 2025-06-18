import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    A = input().strip()
    B = input().strip()
    
    dictA = defaultdict(int)
    
    left = right = 0
    for i in range(1, len(A) + 1):
        nleft = left
        nright = right
        if A[i - 1] == ')':
            if left > 0: nleft -= 1
            else: nright += 1
        else: nleft += 1
            
        if nright > 0: break
        
        dictA[nleft] += 1
        left = nleft
        right = nright
    
    result = 0
    left = right = 0
    for i in range(1, len(B) + 1):
        nleft = left
        nright = right
        if B[i - 1] == ')':
            if left > 0: nleft -= 1
            else: nright += 1
        else: nleft += 1
        
        if nleft == 0:
            result += dictA[nright]
        left = nleft
        right = nright
    
    print(result)

solve()