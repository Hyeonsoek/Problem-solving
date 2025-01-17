c = int(input())
string = input()
r = len(string) // c

k = 0
board = [[''] * c for _ in range(r)]
for i in range(r):
    for j in reversed(range(c)) if i & 1 else range(c):
        board[i][j] = string[k]
        k += 1

result = ''
board = list(zip(*board))
for i in board:
    result += ''.join(i)

print(result)