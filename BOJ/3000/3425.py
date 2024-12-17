import sys

while True:
    ss = []
    while True:
        ss.append(sys.stdin.readline().strip())
        if ss[-1] == 'END':
            break
        if ss[-1] == 'QUIT':
            exit()

    n = int(sys.stdin.readline())
    answer = []

    for i in range(n):
        stack = [int(sys.stdin.readline())]
        for s in ss:
            try:
                if s[:3] == 'NUM':
                    _, n = s.split()
                    stack.append(int(n))
                elif s == 'POP':
                    stack.pop()
                elif s == 'INV':
                    stack[-1] = -stack[-1]
                elif s == 'DUP':
                    stack.append(stack[-1])
                elif s == 'SWP':
                    stack[-1], stack[-2] = stack[-2], stack[-1]
                elif s in ['ADD', 'SUB', 'MUL', 'DIV', 'MOD']:
                    a = stack.pop()
                    b = stack.pop()
                    if s == 'ADD':
                        stack.append(a + b)
                    elif s == 'SUB':
                        stack.append(b - a)
                    elif s == 'MUL':
                        stack.append(a * b)
                    elif s == 'DIV':
                        value = abs(b) // abs(a)
                        if ((a > 0) and (b < 0)) or \
                                ((b > 0) and (a < 0)):
                            value = -value
                        stack.append(value)
                    else:
                        value = abs(b) % abs(a)
                        if b < 0:
                            value = -value
                        stack.append(value)
                else:
                    continue
            except:
                answer.append('ERROR')
                break

        if len(answer) == i+1:
            continue

        if len(stack) == 1 and abs(stack[0]) <= 10**9:
            answer.append(stack[0])
        else:
            answer.append("ERROR")

    for ans in answer:
        print(ans)
    print()