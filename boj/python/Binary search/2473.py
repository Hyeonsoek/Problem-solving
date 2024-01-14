MAX = 3 * (10 ** 9) + 1

n = int(input())
solutions = sorted(list(map(int, input().split())))

min_value = MAX
result = [0, 0, 0]

for x in range(n - 2):
    left, right = x + 1, n - 1
    
    while left < right:
        temp = solutions[x] + solutions[left] + solutions[right]
        
        if min_value >= abs(temp):
            result = [solutions[x], solutions[left], solutions[right]]
            min_value = abs(temp)
            
        if temp < 0:
            left += 1
        elif temp > 0:
            right -= 1
        else:
            break
        
print(*result)