import sys
from collections import defaultdict
ACTG = 'ACTG'
INDEX = {'A': 0, 'C': 1, 'T': 2, 'G': 3}
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    nn = (n*(n-1))//2
    m = len(arr[0])
    
    List = []
    for x in range(4):
        for y in range(x, 4):
            List.append((ACTG[x], ACTG[y]))
    
    Count = defaultdict(int)
    
    for x in range(n):
        for y in range(x + 1, n):
            for i in range(m):
                a = arr[x][i]
                b = arr[y][i]
                if INDEX[a] >= INDEX[b]:
                    a, b = b, a
                Count[a, b] += 1
    
    cache = [[-1] * 321 for _ in range(10)]
    def dynamic(index, value):
        if index == 10:
            return -sys.maxsize if value != 160 else 0
        
        if cache[index][value] != -1:
            return cache[index][value]
        
        xx, yy = List[index]
        result = -sys.maxsize
        if xx == yy:
            for i in range(1, 11):
                result = max(result, dynamic(index + 1, value - i) + Count[xx, yy] * i)
        else:
            for i in range(-10, 11):
                result = max(result, dynamic(index + 1, value - 2 * i) + Count[xx, yy] * i)
        
        cache[index][value] = result
        return result
    
    print(f'{dynamic(0, 160)/nn:.2f}')
    
solve()