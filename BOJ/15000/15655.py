N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

array = []
check = [ 0 for _ in range(N) ]

def bruteforce(repeat):
	if repeat == M:
		print(*array)
	else :
		for x in range(N):
			if (repeat == 0 or (repeat > 0 and array[-1] <= numbers[x]))\
					and check[x] == 0:
				array.append(numbers[x])
				check[x] = 1
				bruteforce(repeat+1)
				check[x] = 0
				array.pop()

bruteforce(0)