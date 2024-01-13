import sys
input = sys.stdin.readline

MAX_POW = 30

while True:
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        break
    
    sparses = [[0 for _ in range(MAX_POW)] for _ in range(n + 1)]
    for idx, value in enumerate(map(int, input().split())):
        sparses[idx + 1][0] = value
        
    for pow in range(1, MAX_POW):
        for number in range(1, n + 1):
            sparses[number][pow] = sparses[ sparses[number][pow - 1] ][pow - 1]
    
    result = list(input())
    indexes = []
    
    for x in range(1, n + 1):
        start, count = x, m
        for pow in range(MAX_POW, -1, -1):
            if count >= (1 << pow):
                count -= (1 << pow)
                start = sparses[start][pow]
        indexes.append(start)
        
    answer = ['' for _ in range(n)]
    for idx in range(n):
        answer[indexes[idx] - 1] = result[idx]
    
    print(''.join(answer))