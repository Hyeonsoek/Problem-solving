decreasing = []

def check_descend(num):
    if len(num) == 1:
        return True

    for i in range(1, len(num)):
        if num[i-1] <= num[i]:
            return False
    return True

def make_descend(string, num):
    global decreasing

    if check_descend(string):
        decreasing.append(string)

    for x in range(num):
        make_descend(string + str(x), x)


for i in range(10):
    make_descend(str(i), i)
decreasing = sorted(decreasing, key=lambda x: int(x))

find = int(input())
print(-1 if len(decreasing) <= find else decreasing[find])