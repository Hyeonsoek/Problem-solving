n, name = input().split()

result = ""
for x in name:
    if x not in result:
        result += x

result = str(1906 + int(n)) + result + str(len(name) - len(result) + 4)
print("smupc_" + result[::-1])