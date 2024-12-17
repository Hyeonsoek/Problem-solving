n = input()

answer = 0

if int(n) >= 10:
	for i in range(1, len(n)):
		answer += i * 9 * (10 ** (i-1))

answer += (int(n) - (10**(len(n)-1)) + 1) * len(n)
print(answer)