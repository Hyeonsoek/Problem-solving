score = [13, 7, 5, 3, 3, 2]

def getScore():
    r = 0
    A = [*map(int, input().split())]
    for x in range(6):
        r += score[x] * A[x]
    return r

if getScore() < getScore() + 1.5:
    print('ekwoo')
else:
    print('cocjr0208')