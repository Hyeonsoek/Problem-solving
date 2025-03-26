def solve():
    n, k = map(int, input().split())
    score = sorted([*map(int, input().split())])
    
    for i in range(k - 1):
        score.pop()
        
    print(score.pop())

solve()