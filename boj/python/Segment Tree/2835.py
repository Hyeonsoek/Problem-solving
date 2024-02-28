import sys
DAY = 86400
HEIGHT = 17
input = sys.stdin.readline

def to_sec(s:str):
    h, m, s = map(int, s.split(":"))
    return h * 3600 + m * 60 + s

def solve():
    n = int(input())
    section = [0] * (DAY + 1)
    for _ in range(n):
        start, _, end = input().split()
        ssec = to_sec(start)
        esec = to_sec(end)
        
        section[ssec] += 1
        if ssec <= esec:
            section[esec + 1] -= 1
        else:
            section[DAY] -= 1
            section[0] += 1
            section[esec + 1] -= 1
        
    tree = [0] * (DAY + 2)
        
    def update(x, value):
        while x <= DAY:
            tree[x] += value
            x += x & -x
    
    def query(x):
        result = 0
        while x > 0:
            result += tree[x]
            x -= x & -x
        return result
    
    for x in range(1, DAY + 1):
        section[x] += section[x - 1]
        update(x, section[x - 1])
    
    result = []
    m = int(input())
    for _ in range(m):
        start, _, end = input().split()
        start_sec = to_sec(start)
        end_sec = to_sec(end)
        
        if start_sec <= end_sec:
            e_sum = query(end_sec + 1)
            s_sum = query(start_sec)
            result.append((e_sum - s_sum) / (end_sec - start_sec + 1))
        else:
            s_to_d = query(DAY) - query(start_sec)
            z_to_e = query(end_sec + 1)
            
            result.append((s_to_d + z_to_e) / (DAY - start_sec + 1 + end_sec))
    
    print(*result, sep='\n')

solve()