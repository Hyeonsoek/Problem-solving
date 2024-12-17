import sys
input = sys.stdin.readline

for _ in range(int(input())):
    column = int(input())
    sticker = [ list(map(int, input().split())) for _ in range(2) ]
    
    if column >= 2:
        sticker[0][1] += sticker[1][0]
        sticker[1][1] += sticker[0][0]
    
        for i in range(2, column):
            sticker[0][i] += max(sticker[1][i-2], sticker[1][i-1])
            sticker[1][i] += max(sticker[0][i-2], sticker[0][i-1])
        
    print(max(list(zip(*sticker))[-1]))