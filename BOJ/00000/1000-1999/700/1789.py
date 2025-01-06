input_s = int(input())

prefix = 0
repeat = 0

while input_s >= prefix + repeat + 1:
    repeat += 1
    prefix += repeat

print(repeat)