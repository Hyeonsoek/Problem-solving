import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    string = input().rstrip()
    
    stack = []
    
    def pop3():
        for x in range(3):
            stack.pop()
    
    def isabb():
        return ''.join(stack[len(stack)-3:len(stack)]) == 'ABB'
    
    for x in range(n):
        stack.append(string[x])
        while len(stack) >= 3 and isabb():
            pop3()
            
            count = 1
            stack.append('B')
            while isabb():
                pop3()
                stack.append('B')
                count += 1
            
            for x in range(count):
                stack.append('A')
                    
    print(''.join(stack))

for _ in range(int(input())):
    solve()