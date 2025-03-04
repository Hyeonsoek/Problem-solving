from collections import deque

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    result = 0
    queue = deque(range(1, n + 1))
    for x in range(m):
        left = 0
        queueleft = deque(queue)
        while True:
            leftpop = queueleft.popleft()
            if leftpop == arr[x]:
                break
            left += 1
            queueleft.append(leftpop)
        
        right = 0
        queueright = deque(queue)
        while True:
            right += 1
            rightpop = queueright.pop()
            if rightpop == arr[x]:
                break
            queueright.appendleft(rightpop)
            
        if left < right:
            result += left
            queue = deque(queueleft)
        else:
            result += right
            queue = deque(queueright)
            
    print(result)
    
solve()