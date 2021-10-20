## ~ing 미완성

string = input()
bomb = input()

stack = []

while True:
    idx = 0
    count = 0
    for s in list(string):
        if s == bomb[idx]:
            if idx == len(bomb) - 1:
                for _ in range(idx):
                    stack.pop()
                idx = 1
                count += 1
            else:
                stack.append((s, idx))
                idx += 1
        else:
            idx = 1
            stack.append((s, 0))

    string = ''.join([stack[i][0] for i in range(len(stack))])
    stack = []

    if count == 0:
        break

print(string if string else "FRULA")