n = int(input())
arr = [input() for _ in range(n)]
m = int(input())
cand = [input() for _ in range(m)]

if n == 1:
    print(cand[0])
    exit(0)

find = arr.index("?")
cand = set(cand) - set(arr)

for x in cand:
    if (not find and arr[1][0] == x[-1]) or\
        (find == n - 1 and arr[find-1][-1] == x[0]) or\
        (0 < find < n and arr[find-1][-1] == x[0] and arr[find+1][0] == x[-1]):
        print(x)
        break