t = int(input())

def win(aa, bb):
	return (aa == 'R' and bb == 'P') \
				or (aa == 'P' and bb == 'S') \
				or (aa == 'S' and bb == 'R')

for _ in range(t):
	c = int(input())
	f, s = 0, 0
	for _ in range(c):
		a, b = input().split()

		if win(b, a):
			f += 1
		if win(a, b):
			s += 1
	
	winner = 1 if f > s else 2
	print('Player {}'.format(winner) if f != s else "TIE")