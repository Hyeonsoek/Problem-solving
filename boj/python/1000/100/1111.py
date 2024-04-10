n = int(input())
recur = list(map(int, input().split()))

if n == 1:
    print('A')
elif n == 2:
    if recur[0] == recur[1]:
        print(recur[0])
    else:
        print('A')
else:
    x = recur[1] - recur[0]
    y = recur[2] - recur[1]
    a = y//x if x else 0
    b = recur[1] - recur[0] * a

    temp = recur[0]
    for i in range(1, n):
        temp = temp * a + b
        if temp != recur[i]:
            print('B')
            exit()

    print(temp * a + b)