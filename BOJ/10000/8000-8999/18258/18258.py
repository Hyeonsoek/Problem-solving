import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

def solve():
    n = int(input())
    queue = deque()

    for _ in range(n):
        query = input().rstrip()
        
        if query[:4] == 'push':
            value = int(query.split()[1])
            queue.append(value)
            continue
        
        match query:
            case 'pop':
                print(f'{queue.popleft() if queue else -1}\n')
            case 'size':
                print(f'{len(queue)}\n')
            case 'empty':
                print(f'{int(not queue)}\n')
            case 'front':
                print(f'{queue[0] if queue else -1}\n')
            case 'back':
                print(f'{queue[-1] if queue else -1}\n')

solve()