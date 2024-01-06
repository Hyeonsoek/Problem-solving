from sys import stdin
from typing import List
input = stdin.readline

def pretty_print(array : List[list]):
    for x in array:
        print(" ".join(map(lambda value : "%5s" % value, x)))
    print("---------------------------------------------------")


w, h, m = map(int, input().split())

rect = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
diamond = [[0 for _ in range(w + 2)] for _ in range(h + 2)]

for _ in range(m):
    values = list(map(int, input().split()))
    
    if values[0] == 1:
        _, px, py, qx, qy = values
        
        rect[py][px] += 1
        rect[py][qx + 1] -= 1
        rect[qy + 1][px] -= 1
        rect[qy + 1][qx + 1] += 1
    else:
        _, px, py, r = values
        
        px += 1

        diamond[py - r][px] += 1
        diamond[py - r + 1][px] += 1
        diamond[py + r + 1][px] += 1
        diamond[py + r + 2][px] += 1
        
        diamond[py + 1][px - r - 1] -= 1
        diamond[py + 1][px - r] -= 1
        diamond[py + 1][px + r] -= 1
        diamond[py + 1][px + r + 1] -= 1
    
# pretty_print(diamond)

#rect imos
for y in range(h + 1):
    for x in range(1, w + 1):
        rect[y][x] += rect[y][x - 1]

for x in range(w + 1):
    for y in range(1, h + 1):
        rect[y][x] += rect[y - 1][x]
        
#diamond imos
#right-up diagonal
for x in range(w + 2):
    yy, xx = 1, x + 1
    while yy < h + 2 and xx < w + 2:
        diamond[yy][xx] += diamond[yy - 1][xx - 1]
        yy, xx = yy + 1, xx + 1

for y in range(1, h + 2):
    yy, xx = y + 1, 1
    while yy < h + 2 and xx < w + 2:
        diamond[yy][xx] += diamond[yy - 1][xx - 1]
        yy, xx = yy + 1, xx + 1

# pretty_print(diamond)

#left-up diagonal
for x in range(w + 2):
    yy, xx = 1, x - 1
    while yy < h + 2 and 0 <= xx:
        diamond[yy][xx] += diamond[yy - 1][xx + 1]
        yy, xx = yy + 1, xx - 1
        
for y in range(1, h + 2):
    yy, xx = y + 1, w
    while yy < h + 2 and 0 <= xx < w + 2:
        diamond[yy][xx] += diamond[yy - 1][xx + 1]
        yy, xx = yy + 1, xx - 1
        
# pretty_print(diamond)

#result
for y in range(h):
    answer = ""
    for x in range(w):
        answer += "#" if (rect[y][x] + diamond[y][x+1]) & 1 else "."
    print(answer)