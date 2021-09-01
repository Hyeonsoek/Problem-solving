N = int(input())
board = [ list(map(int, input().split())) for _ in range(N) ]

MAX = 987654321

route = []
min_cost = MAX
check = [ 0 for _ in range(N) ]

def traveling_salesman(repeat, start, cost):

	global min_cost

	if repeat == N:
		if start != 0 and board[start][0] != 0 and\
				min_cost > cost + board[start][0]:
			min_cost = cost + board[start][0]
	else:
		for x in range(N):
			if x != start and board[start][x] != 0 and check[x] == 0:
				check[x] = 1
				route.append(x)
				traveling_salesman(repeat+1, x, cost + board[start][x])
				check[x] = 0
				route.pop()

check[0] = 1
traveling_salesman(1, 0, 0)
print(min_cost)