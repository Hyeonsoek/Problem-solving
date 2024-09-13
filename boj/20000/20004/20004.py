n = int(input())
for x in range(2, n + 2):
    value = 30 % x
    if value == 0:
        print(x - 1)