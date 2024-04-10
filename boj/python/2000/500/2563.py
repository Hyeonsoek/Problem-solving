b = [[0] * 101 for _ in range(101)]
for _ in range(int(input())):
    x, y = map(int,input().split())
    for s in range(10):
        for t in range(10):
            b[x+s][y+t]=1
print(sum(map(sum, b)))