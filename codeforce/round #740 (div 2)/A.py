t = int(input())

for _ in range(t):
	n = int(input())
	array = list(map(int, input().split()))

	idx = 0
	count = 0
	sorted_arr = sorted(array)

	while idx < n and array != sorted_arr:
		for i in range(idx%2, n, 2):
			if i+1 < n and array[i] > array[i+1]:
				array[i+1], array[i] = array[i], array[i+1]
		count += 1
		idx += 1

	print(count)