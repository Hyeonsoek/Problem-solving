N = int(input())
numbers = list(map(int, input().split()))
counts = list(map(int, input().split()))

MAX = 1000000001

minValue = MAX
maxValue = -MAX

operations = ['+', '-', '*', '//']

def calculate(x1, x2, op):
	if '+' == op:
		return x1 + x2
	if '-' == op:
		return x1 - x2
	if "//" == op:
		if x1 < 0 :
			return -(abs(x1) // x2)
		else :
			return x1 // x2
	if '*' == op:
		return x1 * x2

	return -1

def bruteforce(idx, value):

	global minValue, maxValue

	if idx == N-1:
		if value < minValue:
			minValue = value
		if value > maxValue:
			maxValue = value
	else:
		for x in range(4):
			if counts[x] > 0:
				counts[x] -= 1
				bruteforce(idx+1, calculate(value, numbers[idx+1], operations[x]))
				counts[x] += 1

bruteforce(0, numbers[0])

print(maxValue)
print(minValue)