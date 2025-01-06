from itertools import *

def toint(string, valuedict):
    value = 0
    for x in string:
        value = value * 10 + valuedict[x]
    return value

def solve():
    n = int(input())
    word = [input() for _ in range(n)]
    letters = list(set(''.join(word)))
    first = set([word[x][0] for x in range(n)])
    count = len(letters)
    
    result = 0
    for perm in permutations(range(10), count):
        valuedict = {}
        for x, value in enumerate(perm):
            if letters[x] in first and value == 0:
                break
            valuedict[letters[x]] = value
        else:
            sumvalue = 0
            for x in range(n - 1):
                sumvalue += toint(word[x], valuedict)
            if sumvalue == toint(word[n-1], valuedict):
                result += 1
    
    print(result)
    
solve()