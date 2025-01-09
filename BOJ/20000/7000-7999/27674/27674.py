def solve():
    arr = ''.join(sorted(list(input()), reverse=True))
    n = len(arr)
    
    result = 0
    for x in range(1, n):
        result = max(result, int(arr[:x]) + int(arr[x:]))
    
    print(result)

t = int(input())
for _ in range(t):
    input()
    solve()