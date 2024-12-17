s, t = input(), input()

min_len = len(s)

def brute(string, length):
    if length == min_len:
        return string == s
    else:
        result = False
        if string[-1] == "A":
            result |= brute(string[:-1], length - 1)
        if string[0] == "B":
            result |= brute(string[::-1][:-1], length - 1)
        return result

print(1 if brute(t, len(t)) == True else 0)