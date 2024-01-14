n = int(input())
array = [input() for _ in range(n)]
array.sort(key=lambda x: -len(x))

value = [[] for _ in range(10)]

for _word in array:
    for _digits, _char in enumerate(_word[::-1]):
        value[_digits].append(_char)

dic, Max_Value = {}, 9

for char_array in value[::-1]:
    for char in char_array:
        if char not in dic:
            dic[char] = Max_Value
            Max_Value -= 1

result = 0
for _word in array:
    temp = 0
    for _char in _word:
        temp *= 10
        temp += dic[_char]
    result += temp

print(result)