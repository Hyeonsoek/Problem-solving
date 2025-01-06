import sys
MOD = 1_000_000_007
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arra = list(map(int, input().split()))
    arrb = list(map(int, input().split()))
    
    dicts = {x:[] for x in range(7)}
    for x in range(n):
        target = 7 - arra[x] % 7
        target = target if target < 7 else 0
        dicts[target].append((arra[x], x))
    
    count = n
    prefix = 0
    for x in range(m):
        key = arrb[x] + prefix
        keyMod7 = key % 7
        if count > len(dicts[keyMod7]):
            prefix = key % (MOD * 7)
            count -= len(dicts[keyMod7])
            dicts[keyMod7].clear()
            
    result = []
    for value in dicts.values():
        result += value
    result.sort(key=lambda x: x[1])
    
    print(len(result))
    print(*map(lambda x: (x[0] + prefix) % MOD, result))
    
solve()