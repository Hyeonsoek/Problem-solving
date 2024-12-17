a0, a1 = map(int, input().split())
c = int(input())
n0 = int(input())

for x in range(n0, 200):
    if x * a0 + a1 > c * x:
        print(0)
        break
else:
    print(1)