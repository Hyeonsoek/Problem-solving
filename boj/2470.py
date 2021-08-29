N = int(input())
number = list(map(int, input().split()))

MAX = 2*(10**9)+1

minValue = MAX
answer = None

front, back = 0, N-1

number = sorted(number)
while front < back:

	s = number[front]+number[back]

	if abs(s) < minValue:
		answer = (number[front], number[back])
		minValue = abs(s)

	if s < 0:
		front += 1
	elif s > 0:
		back -= 1
	else:
		break

print(*answer)