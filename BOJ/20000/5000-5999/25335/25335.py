import sys
input = lambda : sys.stdin.readline().split()

def solve():
    n, m = map(int, input())
    for _ in range(n):
        input()
    
    egdes = {'R': 0, 'G': 0, 'B': 0}
    for _ in range(m):
        v, w, c = input()
        egdes[c] += 1
        
    countG = egdes['G']
    countR = egdes['R'] + countG // 2 + (countG & 1)
    countB = egdes['B'] + countG // 2
    
    print('jhnah917' if countR > countB else 'jhnan917')
    
solve()