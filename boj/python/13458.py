import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for x in A:
	t = math.ceil((x-B)/C)
	k = 0 if t < 0 else t
	answer += 1 + k

print(answer)