from sys import stdin

n, m = map(int, stdin.readline().split())
acc_cum = list(map(int, stdin.readline().split()))

for i in range(1, len(acc_cum)):
    acc_cum[i] += acc_cum[i-1]

for _ in range(m):
    i, j = map(int, stdin.readline().split())
    if i == 1:
        print(acc_cum[j-1])
    else:
        print(acc_cum[j-1]-acc_cum[i-2])