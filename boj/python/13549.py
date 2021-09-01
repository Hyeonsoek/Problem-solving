# 0-1 BFS 문제
# 인터넷에 널린 블로그들 너무 난잡하게 써놨다
# 어째서 dijkstra를 써놓고 BFS라고 버젓이 적어놨지?
# dijkstra와 BFS의 차이점을 모르는 건가...

from collections import deque

N, K = map(int, input().split())

def bfs():

	q = deque()
	check = [0 for _ in range(100001)]

	q.append((N,0))

	while q:
		x, time = q.popleft()
		check[x] = 1

		if x == K:
			print(time)
			break

		if 0 <= x - 1 <= 100000 and check[x-1] == 0:
			q.append((x-1, time+1))
			check[x-1] = 1

		if 0 <= x + 1 <= 100000 and check[x+1] == 0:
			q.append((x+1, time+1))
			# check[x+1] = 1 이줄을 추가하면 틀린다. 뭔가 있다.

		if 0 < x * 2 <= 100000 and check[x*2] == 0:
			q.appendleft((x*2, time))
			check[x*2] = 1

bfs()