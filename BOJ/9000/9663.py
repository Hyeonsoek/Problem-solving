N = int(input())

answer = 0
board = [0] * N

def Nqueen(idx):
	global answer
	
	if idx == N:
		answer += 1
		return

	for i in range(N):
		ko = 1
		for j in range(idx):
			if board[j] == i or abs(idx-j) == abs(i-board[j]):
				ko = 0
				break
		if ko:
			board[idx] = i
			Nqueen(idx+1)

Nqueen(0)
print(answer)