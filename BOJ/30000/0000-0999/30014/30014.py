n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

front = 0
back = -1
result_arr = [0] * n
for x in range(n):
    value_back = result_arr[back+1] * arr[x]
    value_front = result_arr[front-1] * arr[x]
    
    if value_front >= value_back:
        result_arr[front] = arr[x]
        front += 1
    else:
        result_arr[back] = arr[x]
        back -= 1

result = 0
for x in range(-1, n - 1):
    result += result_arr[x] * result_arr[x+1]

print(result)
print(*result_arr)