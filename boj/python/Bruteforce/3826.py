import sys
join = [('(', ')'), ('{', '}'), ('[', ']')]
keys = {'(', ')', '[', ']', '{', '}'}
input = sys.stdin.readline

def solve():
    p, q = map(int, input().split())
    
    if p == 0 and q == 0:
        return False
    
    programP = [input().strip() for _ in range(p)]
    programQ = [input().strip() for _ in range(q)]
    
    indent = [0] * p
    for x in range(p):
        count = 0
        while programP[x].startswith((count + 1) * '.'):
            count += 1
        indent[x] = count
    
    countsP = {x: 0 for x in keys}
    values = [[0] * 3 for _ in range(p)]
    for x in range(1, p+1):
        for c in programP[x-1]:
            if c in keys:
                countsP[c] += 1
        
        for y, (left, right) in enumerate(join):
            values[x-1][y] = countsP[left] - countsP[right]

    candidate_rcs = []
    for r in range(1, 21):
        for c in range(1, 21):
            for s in range(1, 21):
                count = 0
                for x in range(1, p):
                    rr, cc, ss = values[x-1]
                    if r * rr + c * cc + s * ss == indent[x]:
                        count += 1
                if count == p - 1:
                    candidate_rcs.append((r, c, s))
    
    result = [0]
    countsQ = {x: 0 for x in keys}
    for x in range(1, q):
        for c in programQ[x-1]:
            if c in keys:
                countsQ[c] += 1
                
        rrccss = []
        candidate_indent = set()
        for left, right in join:
            rrccss.append(countsQ[left] - countsQ[right])
        rr, cc, ss = rrccss

        for r, c, s in candidate_rcs:
            candidate_indent.add(r * rr + c * cc + s * ss)
        
        if len(candidate_indent) == 1:
            result.append(list(candidate_indent)[0])
        else:
            result.append(-1)

    answers.append(result)
    return True

answers = []
while True:
    if not solve():
        break

for x in answers:
    print(*x)