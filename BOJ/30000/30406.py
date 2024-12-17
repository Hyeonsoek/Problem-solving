from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
count = Counter(arr)

dicts = {
    3 : [[0, 3], [1, 2]],
    2 : [[0, 2], [1, 3]],
    1 : [[0, 1], [2, 3]]
}

result = 0
for key, value in dicts.items():
    for p1, p2 in value:
        target = min(count[p1], count[p2])
        result += key * target
        count[p1] -= target
        count[p2] -= target

print(result)