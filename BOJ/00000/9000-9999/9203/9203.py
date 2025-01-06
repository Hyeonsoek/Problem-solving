import sys
from collections import defaultdict
from datetime import datetime, timedelta
input = sys.stdin.readline

def todatetime(yymmdd, hhmm):
    Y, M, D = map(int, yymmdd.split('-'))
    HH, MM = map(int, hhmm.split(':'))
    return datetime(Y, M, D, HH, MM)

def solve():
    b, c = map(int, input().split())
    
    data = defaultdict(int)
    coords = set()
    for x in range(b):
        n, symd, shm, eymd, ehm = input().split()
        start = todatetime(symd, shm)
        end = todatetime(eymd, ehm) + timedelta(minutes=c)
        
        data[start] += 1
        data[end] -= 1
        
        coords.add(start)
        coords.add(end)
        
    coords = sorted(coords)
    
    prefix = 0
    result = 0
    for x in coords:
        prefix += data[x]
        result = max(result, prefix)
    
    print(result)

for _ in range(int(input())):
    solve()