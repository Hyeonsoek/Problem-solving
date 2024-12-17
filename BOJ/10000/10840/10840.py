from collections import defaultdict
MAX = 26

def add(a, b):
    for x in range(MAX):
        a[x] += b[x]

def sub(a, b):
    result = [0] * MAX
    for x in range(MAX):
        result[x] = a[x] - b[x]
    return result

def makeprefix(a, n):
    result = [[0] * MAX for _ in range(n+1)]
    
    for i in range(1, n + 1):
        result[i][ord(a[i-1])-ord('a')] += 1
    
    for i in range(1, n + 1):
        add(result[i], result[i-1])
    
    return result

def solve():
    a = input()
    b = input()
    
    n = len(a); m = len(b)
    A = makeprefix(a, n)
    B = makeprefix(b, m)
    
    H = set()
    
    for l in range(1, n + 1):
        for s in range(l, n + 1):
            string = ','.join(map(str, sub(A[s], A[s-l])))
            H.add(string)
    
    result = 0
    for l in range(1, m + 1):
        for s in range(l, m + 1):
            string = ','.join(map(str, sub(B[s], B[s-l])))
            if string in H:
                result = max(result, l)
                break
    
    print(result)

solve()