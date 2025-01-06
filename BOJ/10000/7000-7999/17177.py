a, b, c = map(int, input().split())

if b < a:
    a, b = b, a

if b < c:
    b, c = c, b
    
ab, bc, cd = a, b, c
ac = (bc * bc - ab * ab)
bd = (bc * bc - cd * cd)
acbd = int((ac * bd) ** .5)

ad = (acbd - ab * cd) // bc

print(-1 if ad < 0 else ad)