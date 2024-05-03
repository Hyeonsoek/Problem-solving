MAX = 100001
che = [ 0 ] * MAX
for x in range(2, MAX):
    for y in range(x * 2, MAX, x):
        che[y] = 1

for _ in range(int(input())):
    m = int(input())
    ans = []

    for j in range(2,m+1):
        if not che[j]:
            count = 0
            while m % j ==0:
                m = m // j
                count += 1
                
            if count:
                ans.append((j, count))

    for a in ans:
        print(*a)