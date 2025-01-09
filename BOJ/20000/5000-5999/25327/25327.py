import sys
input = sys.stdin.readline

subidx = {'kor':0, 'eng':1, 'math':2, '-':3}
fruidx = {'apple':0, 'pear':1, 'orange':2, '-':3}
colidx = {'red':0, 'blue':1, 'green':2, '-':3}

def index(sub, fru, col):
    result = subidx[sub] * 16
    result += fruidx[fru] * 4
    result += colidx[col]
    return result

n, m = map(int, input().split())
setList = [set() for _ in range(64)]

for x in range(n):
    sub, fru, col = input().split()
    for xx in [sub, '-']:
        for yy in [fru, '-']:
            for zz in [col, '-']:
                setList[index(xx, yy, zz)].add(x)

length = [len(setList[x]) for x in range(64)]
    
for _ in range(m):
    sub, fru, col = input().split()
    idx = index(sub, fru, col)
    print(length[idx])