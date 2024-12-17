string = input()
set = set()
len_s = len(string)

for x in range(len_s):
    for l in range(1, len_s+1):
        set.add(string[x:x+l])

print(len(set))