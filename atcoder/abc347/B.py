string = input()
lenS = len(string)

s = set()
for x in range(0, lenS):
    for y in range(x + 1, lenS + 1):
        s.add(string[x:y])
        
print(len(s))