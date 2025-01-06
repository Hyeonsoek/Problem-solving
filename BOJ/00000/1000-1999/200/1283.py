n = int(input())
strings = [ input() for _ in range(n) ]

dicts = {}

def make(index:int, char:str):
    key = char.upper()
    dicts[key] = string[:index]
    dicts[key] += '[' + char + ']'
    dicts[key] += string[index+1:]
    return dicts[key]

for string in strings:
    index = 0
    split = string.split()
    targets : list[tuple[int, str]] = []
    
    for word in split:
        targets.append((index, word[0]))
        index += len(word) + 1
    
    for index, char in enumerate(string):
        if char != " ":
            targets.append((index, char))
            
    for index, char in targets:
        if char.upper() not in dicts:
            print(make(index, char))
            break
    else:
        print(string)