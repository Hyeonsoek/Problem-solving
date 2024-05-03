from string import ascii_uppercase
from itertools import combinations

def make_dicts(s: str):
    dicts = {x: 0 for x in ascii_uppercase}
    for x in s:
        dicts[x] += 1
    return dicts

def compare(to, target):
    for key, value in to.items():
        if target[key] < value:
            return False
    return True

def concat(list_dicts):
    dicts = {x: 0 for x in ascii_uppercase}
    for key in ascii_uppercase:
        for d in list_dicts:
            dicts[key] += d[key]
    return dicts

def solve():
    target = make_dicts(input().strip())
    n = int(input())
    books = []
    for _ in range(n):
        value, name = input().split()
        books.append((int(value), make_dicts(name)))
    
    result = 1e10
    for x in range(1, n + 1):
        for comb in combinations(books, x):
            values, list_dicts = zip(*comb)
            conc = concat(list_dicts)
            if compare(target, conc):
                result = min(result, sum(values))
                
    print(result if result != 1e10 else -1)
    
solve()