from collections import defaultdict

target = input()
n = int(input())

result = 0
resultstr = "Z" * 20
for x in range(n):
    current = input()
    variable = defaultdict(int)
    for char in target + current:
        variable[char] += 1
        
    value = 1
    for c1 in range(3):
        for c2 in range(c1+1, 4):
            value *= variable["LOVE"[c1]] + variable["LOVE"[c2]]
    value %= 100

    if result < value or (result == value and resultstr > current):
        result = value
        resultstr = current

print(resultstr)