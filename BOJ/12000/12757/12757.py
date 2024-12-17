import sys
from bisect import *
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    data = {}
    keys = []
    for _ in range(n):
        key, value = map(int, input().split())
        data[key] = value
        keys.append(key)
    keys.sort()
    
    def findKey(key):
        if keys[0] >= key:
            return keys[0] if keys[0] - key <= k else -1
        
        if keys[-1] <= key:
            return keys[-1] if key - keys[-1] <= k else -1
        
        right = bisect_right(keys, key)
        if keys[right] == key:
            return key
        
        left = right - 1
        lgap = abs(key - keys[left])
        rgap = abs(key - keys[right])
        
        if lgap <= k and rgap <= k:
            if lgap == rgap:
                return '?'
            
            return keys[left] if lgap < rgap else keys[right]
        
        if lgap <= k and rgap > k:
            return keys[left]
        
        if lgap > k and rgap <= k:
            return keys[right]
        
        return -1
                
    r = []
    for _ in range(m):
        q, *arr = map(int, input().split())
        
        match q:
            case 1:
                key, value = arr
                data[key] = value
                insort_right(keys, key)
                n += 1
            case 2:
                key, value = arr
                find = findKey(key)
                if find not in [-1, '?']:
                    data[find] = value
            case 3:
                find = findKey(arr[0])
                if find not in [-1, '?']:
                    r.append(data[find])
                else: r.append(find)
    
    print(*r, sep='\n')
    
solve()