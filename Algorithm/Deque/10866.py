import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
n = int(input())
for x in range(n):
    query = input().split()
    
    match query[0]:
        case "push_front":
            queue.appendleft(query[1])
        case "push_back":
            queue.append(query[1])
        case "pop_front":
            print(queue.popleft() if queue else -1)
        case "pop_back":
            print(queue.pop() if queue else -1)
        case "size":
            print(len(queue))
        case "empty":
            print(0 if queue else 1)
        case "front":
            print(queue[0] if queue else -1)
        case "back":
            print(queue[-1] if queue else -1)