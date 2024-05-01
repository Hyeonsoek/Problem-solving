def solve():
    s, n = map(int, input().split())
    arr = list(map(int, input().split()))

    if s >= n:
        if len(set(arr)) == n:
            return s
        
        count = 0
        
        front = [False] * n
        back = [False] * n
        
        frontSet = set()
        backSet = set()
        for x in range(n):
            frontSet.add(arr[x])
            front[x] = len(frontSet) == x + 1
            
            backSet.add(arr[n-x-1])
            back[x] = len(backSet) == x + 1
            
        for x in range(n-1):
            if front[x] and back[n - x - 2]:
                count += 1
            
        return count
    
    sigma = (s + 1) * s // 2
    
    prefix = [0]
    for x in range(n):
        prefix.append(prefix[-1] + arr[x])

    front = [False] * s
    back = [False] * s
    
    frontSet = set()
    backSet = set()
    for x in range(s):
        frontSet.add(arr[x])
        front[x] = len(frontSet) == x + 1
        
        backSet.add(arr[n-x-1])
        back[x] = len(backSet) == x + 1
    
    count = 0
    for x in range(s):
        if not front[x]:
            continue
        
        back_index = ((n - x - 1) % s) - 1
        if back_index < 0:
            back_index += s
        
        if not back[back_index]:
            continue
            
        rstart = x + 1
        rend = n - back_index - 1
        for start in range(rstart, rend, s):
            end = start + s
            value = prefix[end] - prefix[start]
            if value != sigma:
                break
        else:
            count += 1
    
    return count

t = int(input())
for _ in range(t):
    print(solve())