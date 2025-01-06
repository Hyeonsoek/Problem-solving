def solve():
    n = int(input())
    dic = {char : 0 for char in 'ABCDEFGHIJ'}
    iszero = {char : True for char in 'ABCDEFGHIJ'}

    values = []
    for x in range(n):
        string = input()
        values.append(string)
        for idx, char in enumerate(reversed(string)):
            dic[char] += 10 ** idx
        
        iszero[string[0]] = False


    minKey = min([(value, key) for key, value in dic.items() if iszero[key]])[1]
    newdics = {minKey: '0'}

    count = 0
    sort = sorted([(-value, key) for key, value in dic.items()])

    for _, key in sort:
        if key not in newdics:
            newdics[key] = str(9 - count)
            count += 1

    result = 0
    for xx in range(n):
        value = int(''.join(map(lambda x: newdics[x], list(values[xx]))))
        result += value

    print(result)
    
solve()