from queue import PriorityQueue as PQ
import sys

sys.setrecursionlimit(1000000)

dirr = [[0,1],[0,-1],[1,0],[-1,0]]

def is_finished(board):
	for x in board:
		for y in x:
			if y != 0:
				return False
	return True

def get_distance(board, start_y, start_x, end_y, end_x):

	pq = PQ()
	pq.put((0, start_y, start_x))

	dist = [[987654321] * 4 for _ in range(4)]
	dist[start_y][start_x] = 0

	while not pq.empty():
		cost, y, x = pq.get()

		if dist[y][x] < cost:
			continue

		if y == end_y and x == end_x:
			return cost

		for cnt in range(1, 4):
			for ydir, xdir in dirr:
				xx = x + xdir * cnt
				yy = y + ydir * cnt

				if 0 <= xx < 4 and 0 <= yy < 4:
					if board[yy][xx] == 0 and dist[yy][xx] > cost + cnt:
						dist[yy][xx] = cost + cnt
						pq.put((cost+cnt, yy, xx))
					
					if ((yy == 0 or yy == 3 or xx == 0 or xx == 3) or board[yy][xx] != 0)\
							and dist[yy][xx] > cost + 1:
						dist[yy][xx] = cost + 1
						pq.put((cost+1, yy, xx))

	return -1


def solve(board, y, x):
	if is_finished(board):
		return 0

	ret = 987654321

	for k in range(1,7):
		point = []
		for i in range(0,4):
			for j in range(0,4):
				if board[i][j] == k:
					point.append((i,j))

		if not point:
			continue

		first = get_distance(board, y, x, point[0][0], point[0][1]) +\
					get_distance(board, point[0][0], point[0][1], point[1][0], point[1][1]) + 2

		second = get_distance(board, y, x, point[1][0], point[1][1]) +\
			 		get_distance(board, point[1][0], point[1][1], point[0][0], point[0][1]) + 2

		board[point[0][0]][point[0][1]] = 0
		board[point[1][0]][point[1][1]] = 0

		ret = min(first + solve(board, point[1][0], point[1][1]),
					second + solve(board, point[0][0], point[0][1]), ret)

		board[point[0][0]][point[0][1]] = k
		board[point[1][0]][point[1][1]] = k

	return ret

def solution(board, r, c):
	answer = solve(board, r, c)
	return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],0,1))
print(solution([[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]], 0, 0))