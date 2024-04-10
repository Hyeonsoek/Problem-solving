N, M = map(int, input().split())

array = []

def bruteforce(repeat):
	if repeat == M:
		print(*array)
	else :
		for x in range(N):
			if repeat == 0 or (repeat >= 1 and array[-1] <= x+1):
				array.append(x+1)
				bruteforce(repeat+1)
				array.pop()

bruteforce(0)