cache = [1 for _ in range(10)]

for _ in range(int(input())):
    for i in range(1, 10):
        cache[i] += cache[i-1]
        cache[i] %= 10007
        
print(cache[-1])