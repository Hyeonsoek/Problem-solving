n = int(input())
string = [list(input()) for _ in range(n)]

answer = string[0]

for j in range(1, n):
    for i in range(len(string[0])):
        if string[j][i] != answer[i]:
            answer[i] = '?'

print(''.join(answer))