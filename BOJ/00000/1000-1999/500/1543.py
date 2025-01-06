string = input()
find = input()

result = 0
index = 0

while index < len(string)-len(find)+1:
    if string[index:index+len(find)] == find:
        result += 1
        index += len(find)
    else:
        index += 1

print(result)