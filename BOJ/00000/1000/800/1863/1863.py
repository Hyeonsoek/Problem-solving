import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    point = [tuple(map(int, input().split())) for _ in range(n)]
    
    point.sort()
    point = [ point[x][1] for x in range(n) ]
    
    result = 0
    stack = []
    for x in range(n):
        if stack and stack[-1] > point[x]:
            while stack and stack[-1] > point[x]:
                stack.pop()
                result += 1

        if (not stack or (stack and stack[-1] < point[x])) and point[x] > 0:
            stack.append(point[x])
    
    print(result + len(stack))

solve()