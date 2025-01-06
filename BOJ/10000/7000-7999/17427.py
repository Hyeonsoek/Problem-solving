n = int(input())

result = 0
for x in range(1, n + 1):
    result += (n // x) * x
    
print(result)