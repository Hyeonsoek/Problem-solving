def solve():
    n = int(input())
    arr = list(map(lambda x: ord(x) - ord('a'), input()))
    k = len(arr)
    
    count = [0] * 26
    count[arr[0]] += 1
    result = 0
    front, back = 0, 0
    while front <= back < k:
        kind = 0
        for x in range(26):
            kind += count[x] > 0
        
        if kind <= n:
            result = max(result, back - front + 1)
            
        if kind > n:
            count[arr[front]] -= 1
            front += 1
        else:
            back += 1
            if back < k:
                count[arr[back]] += 1
        
    print(result)

solve()