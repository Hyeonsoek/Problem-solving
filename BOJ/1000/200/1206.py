def solve():
    n = int(input())
    arr = [ int(input().replace('.','')) for _ in range(n) ]

    for count in range(1, 1001):
        dicts = set()
        for s in range(count * 10 + 1):
            value = (s * 1000) // count
            dicts.add(value)
        
        for x in arr:
            if x not in dicts:
                break
        else:
            return count
        
print(solve())