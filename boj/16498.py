A, B, C = map(int, input().split())

Acards = sorted(list(map(int, input().split())))
Bcards = sorted(list(map(int, input().split())))
Ccards = sorted(list(map(int, input().split())))

MAX = 200000001
minValue = MAX

curA, curB, curC = 0, 0, 0

while curA < A and curB < B and curC < C:

	# print(curA, curB, curC)

	temp = [Acards[curA], Bcards[curB], Ccards[curC]]
	value = abs(max(temp) - min(temp))

	if minValue > value:
		minValue = value

	if min(temp) == Acards[curA]:
		curA += 1
	elif min(temp) == Bcards[curB]:
		curB += 1
	elif min(temp) == Ccards[curC]:
		curC += 1

print(minValue)