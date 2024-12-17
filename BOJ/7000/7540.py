def solve():
    time, problem = map(int, input().split())
    diff = sorted(list(map(int, input().split())))
    
    curr = 0
    count = 0
    score = 0
    for x in range(problem):
        curr += diff[x]
        if curr <= time:
            score += curr
            count += 1
    
    return f'Steve wins with {count} solved problems and a score of {score}.\n'
    
t = int(input())
for x in range(1, t + 1):
    result = solve()
    print(f"Scenario #{x}:")
    print(result)