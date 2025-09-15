import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    k = int(input())

    if k == 1:
        print(*sorted(arr))
        return
    
    answer = []
    s = 0
    e = n // k
    for i in range(k):
        answer.extend(sorted(arr[s : e]))
        s += n // k
        e += n // k
        
    print(*answer)

solve()