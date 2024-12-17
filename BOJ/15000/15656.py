N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

array = []

def bruteforce(repeat):
	if repeat == M:
		print(*array)
	else :
		for x in range(N):
			array.append(numbers[x])
			bruteforce(repeat+1)
			array.pop()

bruteforce(0)