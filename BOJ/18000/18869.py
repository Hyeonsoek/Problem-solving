import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
result = defaultdict(int)

for _ in range(n):
    space = list(map(int, input().split()))
    compressed = sorted(list(set(space)))
    dic = {value : idx for idx, value in enumerate(compressed)}
    compress = " ".join(str(dic[space[x]]) for x in range(m))
    result[compress] += 1
    
answer = 0
for value in result.values():
    answer += (value - 1) * value // 2
print(answer)