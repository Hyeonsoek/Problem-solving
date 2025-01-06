n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

result = 1
for x in range(1, n + 1):
    result = max(result, arr[x-1] + x)
    
print(result + 1)