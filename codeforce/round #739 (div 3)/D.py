MAX = 987654321

t = int(input())

for _ in range(t):
	number = input()
	answer = MAX

	for two in range(60):
		two = str(2**two)

		idx, cost = 0, 0

		for t in two:
			while idx < len(number) and number[idx] != t:
				idx += 1
			if idx < len(number) and number[idx] == t:
				cost += 1
				idx += 1

		answer = min(answer, len(number) + len(two) - cost * 2 )

	print(answer)