import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    q = int(input())
    stack = defaultdict(list)
    
    for _ in range(q):
        qq, i = map(int, input().split())
        
        match qq:
            case 1:
                yaxis = 0
                for x in range(i, i + 4):
                    if x in stack and stack:
                        yaxis = max(yaxis, stack[x][-1])
                for x in range(i, i + 4):
                    stack[x].append(yaxis + 1)
            case 2:
                yaxis = stack[i][-1] if i in stack else 0
                for x in range(i, i + 4):
                    stack[i].append(yaxis + x - i + 1)
            case 3:
                print(stack[i][-1] if i in stack else 0)

solve()