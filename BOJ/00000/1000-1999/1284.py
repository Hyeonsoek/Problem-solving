from sys import stdin
input = stdin.readline
l = [3] * 10
l[0] = 4
l[1] = 2

while True:
    n = input().strip()
    if n == '0':
        break
    n = list(map(int, n))
    result = len(n) + 1
    for x in n:
        result += l[x]
    print(result)