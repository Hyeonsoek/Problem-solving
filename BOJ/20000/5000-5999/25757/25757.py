import sys
input = sys.stdin.readline

def sovle():
    n, game = input().split()
    n = int(n)
    game = {'Y':1, 'F':2, 'O':3}[game]

    count = 0
    stack = []
    name = set()
    for x in range(n):
        apply = input().rstrip()
        if apply not in name:
            name.add(apply)
            stack.append(apply)
            if len(stack) == game:
                count += 1
                stack.clear()

    print(count)

sovle()