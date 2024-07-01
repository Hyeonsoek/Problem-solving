n, s, r = map(int, input().split())
broken = list(map(int, input().split()))
hasmore = list(map(int, input().split()))

kayak = [1] * (n + 1)
for x in broken:
    kayak[x] -= 1

for x in hasmore:
    kayak[x] += 1
    
for x in range(1, n + 1):
    if kayak[x] > 1:
        if x > 1 and not kayak[x-1]:
            kayak[x-1] += 1
            kayak[x] -= 1
        elif x < n and not kayak[x+1]:
            kayak[x+1] += 1
            kayak[x] -= 1

result = 0
for x in range(1, n + 1):
    result += kayak[x] == 0

print(result)