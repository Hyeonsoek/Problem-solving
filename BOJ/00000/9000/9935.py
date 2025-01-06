string = input()
bomb = input()

stack = []

for s in string:
    stack.append(s)
    if len(stack) >= len(bomb) and bomb == ''.join(stack[len(stack)-len(bomb):]):
        for _ in range(len(bomb)):
            stack.pop()

print(''.join(stack) if stack else 'FRULA')