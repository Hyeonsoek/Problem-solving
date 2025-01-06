def transform(string):
    length = len(string)
    
    value = 0
    for x in range(length):
        if '0' <= string[x] <= '9':
            value += int(string[x])
    
    return length, value, string

n = int(input())
arr = sorted([transform(input()) for _ in range(n)])

for item in arr:
    print(item[2])