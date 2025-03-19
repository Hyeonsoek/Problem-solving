chars = 'ABDOPQRabdegopq@'
counts = '1211111111111111'
data = { chars[i] : int(counts[i]) for i in range(len(chars)) }

def tovalue(string):
    result = 0
    for i in string:
        if i in data:
            result += data[i]
    return result

print(tovalue(input()))