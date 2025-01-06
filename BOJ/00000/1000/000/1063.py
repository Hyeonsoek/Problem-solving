direct = {
    'R':(1, 0), 'L':(-1, 0), 'T':(0, 1), 'B':(0, -1), 
    'RB':(1, -1), 'LB':(-1, -1), 'RT':(1, 1), 'LT':(-1, 1)
}

def position(pos):
    col, row = pos[0], pos[1]
    return ord(col) - ord('A') + 1, int(row)

def to_string(x, y):
    return chr(x + ord('A') - 1) + str(y)

king, stone, n = input().split()
kx, ky = position(king)
sx, sy = position(stone)
n = int(n)

for x in range(n):
    xdir, ydir = direct[input()]
    kkx, kky = kx + xdir, ky + ydir
    ssx, ssy = sx + xdir, sy + ydir
    
    if 0 < kkx < 9 and 0 < kky < 9:
        if kkx == sx and kky == sy:
            if 0 < ssx < 9 and 0 < ssy < 9:
                kx, ky = kkx, kky
                sx, sy = ssx, ssy
        else:
            kx, ky = kkx, kky

print(to_string(kx, ky))
print(to_string(sx, sy))