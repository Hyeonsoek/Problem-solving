import sys

sys.setrecursionlimit(1000000)

N = int(input())
string = input()

stack = [(0, 0, N)]
board = [ [0 for _ in range(N)] for _ in range(N) ]

def daq(idx):
	if idx < len(string):
		if string[idx] == 'Q':
			y, x, n = stack.pop()
			n //= 2
			stack.append((y+n, x+n, n))
			stack.append((y+n, x, n))
			stack.append((y, x+n, n))
			stack.append((y, x, n))
		else:
			y, x, n = stack.pop()
			for yy in range(y, y + n):
				for xx in range(x, x + n):
					board[yy][xx] = '1' if string[idx] == 'B' else '0'

		daq(idx+1)

daq(0)

print('#define quadtree_width {}'.format(N))
print('#define quadtree_height {}'.format(N))
print('static char quadtree_bits[] = {')
for y in board:
	for xx in range(0, N, 8):
		print("0x"+f"{int(''.join(y[xx:xx+8][::-1]),2):x}".zfill(2), end=',')
	print()
print('};')