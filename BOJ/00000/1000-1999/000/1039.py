from collections import deque

def get_value(digits, a, b):
    value = digits[:]
    value[a] = digits[b]
    value[b] = digits[a]
    return int("".join(value))

def solve():
    n, k = map(int, input().split())
    m = len(str(n))
    
    result = -1
    visited = [[0] * 1000001 for _ in range(k)]
    queue = deque([(n, 0)])
    while queue:
        value, count = queue.popleft()
        
        if count == k:
            result = max(result, value)
            continue
        
        digits = list(str(value))
        for x in range(m):
            for y in range(x + 1, m):
                if y == 0 and digits[x] == '0':
                    continue
                
                if x == 0 and digits[y] == '0':
                    continue
        
                nextValue = get_value(digits, x, y)
                if not visited[count][nextValue]:
                    visited[count][nextValue] = 1
                    queue.append((nextValue, count + 1))
    
    print(result)
    
solve()