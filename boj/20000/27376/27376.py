import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    arr = sorted([[0, 0, 0]] + [[*map(int, input().split())] for _ in range(k)])
    
    time = 0
    position = 0
    for x in range(1, k + 1):
        pos, t, start = arr[x]
        time += pos - position
        position = pos
        
        if time >= start:
            x = (time - start) % (2 * t)
            if t <= x:
                time += 2 * t - x
        else:
            time += start - time
    
    time += n - arr[-1][0]
    
    print(time)
    
solve()