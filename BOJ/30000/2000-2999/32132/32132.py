n = int(input())
string = [*input()]

stack = []
for x in range(n):
    stack.append(string[x])
    if len(stack) >= 3:
        xx = ''.join(stack[-3:])
        if xx == 'PS4' or xx == 'PS5':
            stack.pop()

print(''.join(stack))