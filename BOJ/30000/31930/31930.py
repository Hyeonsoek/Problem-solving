import sys
input = sys.stdin.readline

def output(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def query(l, r):
    output(f'AK {l} {r}\n')
    return input().strip()

def binary_search(l, r):
    while l < r:
        mid = (l + r) // 2
        value = query(l, mid)
        
        if value == 'O':
            r = mid
        else:
            l = mid + 1
    
    return l

def solve():
    n = int(input())
    k = n // 2
    
    if query(1, k) == 'O':
        a = binary_search(1, k)
        b = binary_search(k + 1, n)
        output(f'! {a} {b}\n')
    else:
        for i in range(2, n):
            l, r = i, i + k - 1
            
            if r > n:
                break
            
            value = query(l, r)
            
            if value == 'O':
                if query(l - 1, l - 1) == 'O':
                    a = binary_search(l, k)
                    b = l - 1
                    output(f'! {a} {b}\n')
                else:
                    a = binary_search(r + 1, n)
                    b = r
                    output(f'! {a} {b}\n')
                break

t = int(input())
for _ in range(t):
    solve()