import sys, collections
input = sys.stdin.readline

def solve():
    n = int(input())
    queue = collections.deque()
    
    result = []
    for _ in range(n):
        query = input().split()
        
        match query[0]:
            case "1":
                queue.appendleft(query[1])
            case "2":
                queue.append(query[1])
            case "3":
                result.append(queue.popleft() if queue else -1)
            case "4":
                result.append(queue.pop() if queue else -1)
            case "5":
                result.append(len(queue))
            case "6":
                result.append(0 if queue else 1)
            case "7":
                result.append(queue[0] if queue else -1)
            case "8":
                result.append(queue[-1] if queue else -1)
    
    print(*result, sep='\n')

solve()