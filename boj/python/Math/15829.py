n = int(input())
string = input()

result = 0
for x in range(n):
    result += (ord(string[x]) - 96) * (31 ** x)
    result %= 1234567891
print(result)