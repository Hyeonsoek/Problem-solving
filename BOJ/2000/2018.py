n = int(input())
count = 0

for x in range(n):
    value = x * (x + 1) // 2
    if value >= n:
        break
    
    if (n - value) % (x + 1) == 0:
        count += 1

print(count)