n = int(input())
a = list(map(int, input().split()))
b = sum(map(lambda x: ((x//60)+1)*15, a))
c = sum(map(lambda x: ((x//30)+1)*10, a))

if b == c:
    print("Y M", b)
else:
    if b < c:
        print("M", b)
    else:
        print("Y", c)