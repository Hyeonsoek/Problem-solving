def solve(n):
    names = []
    papers = [['P'] * n for _ in range(n)]
    for x in range(n):
        name, *score = input().split()
        names.append(name)
        
        for xx in range(x-1, x-n, -1):
            papers[x][xx % n] = score[abs(xx-x+1)]
            
    result = []
    for x in range(n):
        for xx in range(x-1, x-n, -1):
            if papers[x][xx] == 'N':
                result.append(f'{names[xx]} was nasty about {names[x]}')
    
    if not result:
        result.append("Nobody was nasty")
    
    return result

c = 1
while True:
    n = int(input())
    if not n:
        break
    
    print(f'Group {c}')
    print(*solve(n), sep='\n')
    print()
    
    c += 1