k, n = map(int, input().split())
ran = [int(input()) for _ in range(k)]

answer = -1
low, high = 1, 2**31-1

while low <= high:
	mid = (low+high)//2

	count = 0
	for r in ran:
		count += r//mid

	if count >= n:
		low = mid+1
		if mid > answer:
			answer = mid
	elif count < n:
		high = mid-1

print(answer)