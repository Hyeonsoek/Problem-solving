N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

result = set()
array = []

def bruteforce(repeat):
	if repeat == M:
		result.add(tuple(array[:]))
	else :
		for x in range(N):
			if repeat == 0 or (repeat > 0 and array[-1] <= numbers[x]):
				array.append(numbers[x])
				bruteforce(repeat+1)
				array.pop()

bruteforce(0)

result = sorted(list(result))

for x in result:
	print(*x)