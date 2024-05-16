from string import ascii_uppercase as upper

n, q = map(int, input().split())
arr = list(input())

nextcase = {upper[x]: upper[(x+1)%26] for x in range(26)}

def update(left, right):
    for x in range(left, right + 1):
        arr[x] = nextcase[arr[x]]

def query(left, right):
    result = 1
    for x in range(left + 1, right + 1):
        result += 1 if ord(arr[x]) - ord(arr[x-1]) != 0 else 0
    return result

for _ in range(q):
    qq, l, r = map(int, input().split())
    if qq & 1:
        print(query(l-1, r-1))
    else:
        update(l-1, r-1)