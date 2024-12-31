def to_string(value):
    result = ''
    for x in range(13):
        result = chr(value % 26 + 97) + result
        value //= 26
    return result

def get_ab(string):
    value = 0
    for x, c in enumerate(string[::-1]):
        value += (ord(c) - 97) * (26 ** x)
    return value

match int(input()):
    case 1:
        print(to_string(sum(map(int, input().split()))))
    case 2:
        print(get_ab(input()))