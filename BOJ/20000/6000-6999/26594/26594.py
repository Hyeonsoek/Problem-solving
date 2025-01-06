count = 0
string = input()
char = string[0]
for x in string:
    if char != x:
        break
    count += 1
print(count)