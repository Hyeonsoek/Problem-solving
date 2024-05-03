N = int(input())
numbers = list(map(int, input().split()))

def next_permutation(array):
	i, j = len(array) - 1, len(array) - 1

	while i > 0 and array[i-1] >= array[i]:
		i -= 1

	if i == 0:
		return False

	while array[i-1] >= array[j]:
		j -= 1

	array[i-1], array[j] = array[j], array[i-1]

	k = len(array) - 1

	while i < k :
		array[i], array[k] = array[k], array[i]

		i += 1
		k -= 1

	return array

result = next_permutation(numbers)

if result:
	print(*result)
else:
	print(-1)