from collections import deque

n, m = map(int, input().split())
arr = deque(sorted(list(map(int, input().split())), reverse=True))

result = 0
for x in range(min(n, m)):
    if not arr or arr[0] < 0:
        break
    
    result += arr.popleft()
    
    if not arr:
        break
    
    arr.pop()
    
print(result)