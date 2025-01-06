def solve(): 
    lower = "abcdefghijklmnopqrstuvwxyz"
    target = input()
    n = len(target)

    index = 0
    result = 0
    while index < n:
        result += 1
        for x in lower:
            if index < n and target[index] == x:
                index += 1

    print(result)

solve()