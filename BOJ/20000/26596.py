import sys
from math import *
input = sys.stdin.readline

def solve():
    m = int(input())

    dic = {}
    names = []
    for _ in range(m):
        name, value = input().split()
        if name not in dic:
            names.append(name)
            dic[name] = int(value)
        else:
            dic[name] += int(value)

    n = len(names)
    for x in range(n):
        for y in range(n):
            if x == y: continue
            
            if floor(dic[names[x]] * 1.618) == dic[names[y]]:
                return "Delicious!"
    
    return "Not Delicious..."

print(solve())