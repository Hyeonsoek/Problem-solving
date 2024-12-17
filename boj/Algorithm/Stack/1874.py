import sys
input = sys.stdin.readline

n = int(input())
array = [ int(input()) for _ in range(n) ]

top, index = 1, 0
result = []
stack = []
for _ in range(2*n):
    if stack and array[index] == stack[-1]:
        index += 1
        result.append('-')
        stack.pop()
    else:
        result.append('+')
        stack.append(top)
        top += 1

if not stack:
    print(*result, sep='\n')
else:
    print("NO")