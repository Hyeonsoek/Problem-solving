from itertools import combinations

def gcd(a, b):
	return gcd(b, a%b) if b else a

for _ in range(int(input())):
	temp = list(map(int, input().split()))
	temp = list(combinations(temp[1:], 2))

	gcd_sum = 0
	for x, y in temp:
		gcd_sum += gcd(x, y)

	print(gcd_sum)