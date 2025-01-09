from collections import deque

S = int(input())

def bfs():

	q = deque()
	check = [ [0 for _ in range(S+1)] for _ in range(S+1) ]

	q.append((1, 0, 0))
	check[1][0] = 1

	answer = 987654321

	while q:
		count, clipboard, time = q.popleft()

		if count == S and answer > time:
			answer = time
			break

		# 1 copy
		if check[count][count] == 0:
			q.append((count, count, time+1))
			check[count][count] = 1

		# 2 paste
		if clipboard and count + clipboard <= S and\
				check[count + clipboard][clipboard] == 0:
			q.append((count + clipboard, clipboard, time+1))
			check[count + clipboard][clipboard] = 1

		# 3 delete
		if 0 < count - 1 and check[count - 1][clipboard] == 0:
			q.append((count - 1, clipboard, time+1))
			check[count - 1][clipboard] = 1

	return answer

print(bfs())