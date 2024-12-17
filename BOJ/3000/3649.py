import sys

MIN = -1

while True:
	try:
		x = int(sys.stdin.readline())
		n = int(sys.stdin.readline())
		blocks = [int(sys.stdin.readline()) for _ in range(n)]

		minValue = MIN
		answer = None

		front, back = 0, n-1
		blocks = sorted(blocks,reverse=True)

		while 0 <= back and front < n and front < back:

			s = (blocks[front]+blocks[back])/10000000

			if s > x:
				front += 1
			elif s < x:
				back -= 1
			else:
				answer = (blocks[front], blocks[back])
				break

		if answer:
			print('yes',*sorted(answer))
		else:
			print('danger')
	except:
		break