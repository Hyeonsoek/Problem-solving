import sys
input = sys.stdin.readline

def solve():
    string = input().strip()
    
    columnF = [270, 0, 90]
    columnR = [90, 180, 270]
    rowF = [180, 270, 0]
    rowR = [0, 90, 180]
    
    degree = [0]
    for x in string + string[:2]:
        if x == 'L':
            degree.append((degree[-1] - 90) % 360)
        else:
            degree.append((degree[-1] + 90) % 360)
    
    xx, yy = 1, 1
    for x in range(2, len(degree)):
        tt = degree[x-2:x+1]
        if tt == columnF or tt == columnR:
            xx = 0

        if tt == rowF or tt == rowR:
            yy = 0

    print(xx + yy)
    

for _ in range(int(input())):
    solve()