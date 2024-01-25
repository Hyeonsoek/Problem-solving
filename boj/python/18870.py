import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
compress = sorted(list(set(array)))
dic = { x : idx for idx, x in enumerate(compress) }

print(*(dic[x] for x in array))