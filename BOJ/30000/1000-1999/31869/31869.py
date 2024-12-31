n = int(input())

schedule = {}
calander = [0] * (10 * 7)

for _ in range(n):
    S, *number = input().split()
    W, D, P = map(int, number)
    index = (W - 1) * 7 + D
    schedule[S] = (index, P)
    
for _ in range(n):
    name, cash = input().split()
    
    index, PP = schedule[name]
    calander[index] = max(calander[index], 1 if PP <= int(cash) else 0)

result = 0
for x in range(1, 70):
    if calander[x]:
        calander[x] += calander[x-1]

print(max(calander))