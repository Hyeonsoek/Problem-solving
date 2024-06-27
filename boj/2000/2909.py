c, k = map(int, input().split())
value = c / 10 ** k

if value - int(value) < 0.5:
    value = int(value)
else:
    value = int(value) + 1
    
print(value * 10 ** k)