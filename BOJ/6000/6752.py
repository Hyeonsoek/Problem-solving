t = int(input())
c = int(input())
arr = sorted([int(input()) for _ in range(c)])

time = 0
count = 0
for x in range(c):
    time += arr[x]
    if time <= t:
        count += 1
        
print(count)