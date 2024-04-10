from itertools import permutations

def get_difference(lst):

	difference = 0

	for x in range(len(lst)-1):
		difference += abs(lst[x] - lst[x+1])

	return difference

N = int(input())

numbers = list(map(int, input().split()))
numbers_per = list(permutations(numbers))

answer = -1

for lst in numbers_per:
	answer = max(answer, get_difference(lst))

print(answer)