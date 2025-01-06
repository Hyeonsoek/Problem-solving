import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    
    stack = []
    result = []
    for _ in range(n):
        query = [*map(int, input().split())]
        
        match query[0]:
            case 1:
                stack.append(query[1])
            case 2:
                result.append(stack.pop() if stack else -1)
            case 3:
                result.append(len(stack))
            case 4:
                result.append(0 if stack else 1)
            case 5:
                result.append(stack[-1] if stack else -1)
    
    print(*result, sep='\n')
    
solve()