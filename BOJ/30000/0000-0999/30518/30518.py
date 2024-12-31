from itertools import combinations

lose = {'R':'P', 'P':'S', 'S':'R'}
win = {'R':'S', 'P':'R', 'S':'P'}

lighter = input()
smallant = input()

def is_correct(comb):
    s = "".join(comb)
    l = lighter + s[:-1]
    
    length = len(s)
    result = [0] * length
    for x in range(length):
        if lose[s[x]] == l[x]:
            result[x] -= 1
        
        if win[s[x]] == l[x]:
            result[x] += 1
    
    for x in range(1, length):
        if result[x-1] == -1 and result[x] == 0:
            return False
    
    return True

count = 0

for x in range(1, len(smallant)+1):
    for comb in combinations(smallant, x):
        if is_correct(comb):
            count += 1

print(count)