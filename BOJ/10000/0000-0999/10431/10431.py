def solve():
    n, *arr = map(int, input().split())

    count = 0
    result = [arr[0]]
    for x in range(1, 20):
        for y in range(x):
            if result[y] > arr[x]:
                count += len(result) - y
                result.insert(y, arr[x])
                break
        else:
            result.append(arr[x])
    
    print(n, count)

for _ in range(int(input())):
    solve()