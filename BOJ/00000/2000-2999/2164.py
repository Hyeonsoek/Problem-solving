from collections import deque

n = int(input())
array = deque(range(1, n + 1))

while True:
    if len(array) == 1:
        break
    
    x = array.popleft()
    array.append(array.popleft())
    
print(array[0])