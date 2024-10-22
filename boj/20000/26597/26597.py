import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    result = 0
    arr = [input().split() for _ in range(n)]
    left, right = -10**18, 10**18
    for x in range(n):
        value, char = arr[x]
        value = int(value)
        if char == '^':
            left = max(value + 1, left)
        else:
            right = min(value - 1, right)
        
        if left > right:
            return f'Paradox!\n{x+1}'
    
        if result == 0 and right - left == 0:
            result = x + 1
    
    if result > 0:
        return f'I got it!\n{result}'
    
    return 'Hmm...'

print(solve())