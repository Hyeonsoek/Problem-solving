test = int(input())

for _ in range(test):
	t = input()

	answer = None
	low, high = 0, len(t)-1

	while low <= high:
		mid = (low+high)//2

		string = make_trans(t[:mid+1])

		if t == string:
			answer = mid
			break
		else:
			if 