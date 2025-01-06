def solve():
    s, p = input().split()
    
    x = 0
    result = 0
    while x < len(s):
        if s[x:x+len(p)] == p:
            x += len(p)
        else:
            x += 1

        result += 1

    print(result)

for _ in range(int(input())):
    solve()