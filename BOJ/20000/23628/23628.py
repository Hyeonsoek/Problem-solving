sy, sm, sd = map(int, input().split())
ey, em, ed = map(int, input().split())

def to_day(yy, mm, dd):
    return yy * 360 + mm * 30 + dd

start = to_day(sy, sm, sd)
end = to_day(ey, em, ed)

day = end - start

y, m = 0, min(36, ((end - start) // 30))
for x in range(start + 360, end + 1, 360):
    y += ((((x - start) // 360) - 1) // 2) + 15
    
print(y, m)
print(f'{day}days')