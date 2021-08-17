from collections import deque
from collections import defaultdict

A, B, C = map(int, input().split())

def bfs():

	answer = []
	q = deque()
	check = defaultdict(int)

	q.append('0/0/'+str(C))
	check['0/0/' + str(C)] = 1

	while q:
		a, b, c = map(int, q.popleft().split('/'))

		arrays = []

		if a == 0:
			answer.append(c)

		if a < A:
			if b > 0:
				arrays.append([a+b, 0, c] if a + b <= A else [A, a+b-A, c])
			if c > 0:
				arrays.append([a+c, b, 0] if a + c <= A else [A, b, a+c-A])

		if b < B:
			if a > 0:
				arrays.append([0, a+b, c] if a + b <= B else [a+b-B, B, c])
			if c > 0:
				arrays.append([a, c+b, 0] if c + b <= B else [a, B, c+b-B])

		if c < C:
			if a > 0:
				arrays.append([0, b, a+c] if a + c <= C else [a+c-C, b, C])
			if b > 0:
				arrays.append([a, 0, b+c] if b + c <= C else [a, b+c-C, C])

		for array in arrays:
			string = '/'.join(list(map(str, array)))

			if check[string] == 0:
				check[string] = 1
				q.append(string)

	return answer

print(*sorted(list(set(bfs()))))