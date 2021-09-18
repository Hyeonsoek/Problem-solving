blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]
red = [[0] * 4 for _ in range(4)]

def monominodomino(t, x, y):
    global blue, green
    clear = 0

    # blue in


    # green in


    return clear


# print(''.join(map(str, blue[0])))

score = 0
n = int(input())
for _ in range(n):
    tt, xx, yy = map(int, input().split())
    score += monominodomino(tt, xx, yy)

print(score)

block = 0
for i in range(4):
    for j in range(6):
        if blue[i][j] == 1:
            block += 1

for i in range(6):
    for j in range(4):
        if green[i][j] == 1:
            block += 1

print(block)