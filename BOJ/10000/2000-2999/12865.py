N, K = map(int, input().split())

knapsack = [ list(map(int, input().split())) for _ in range(N) ]

def knapsack_dp():

	global N, K, knapsack
	cache = [[0 for _ in range(K+1)] for _ in range(N+1)]

	for i in range(1, N+1):
		for j in range(1, K+1):
			if knapsack[i-1][0] <= j:
				cache[i][j] = max(knapsack[i-1][1] + cache[i-1][j-knapsack[i-1][0]],
									cache[i-1][j])
			else:
				cache[i][j] = cache[i-1][j]

	return cache[N][K]

print(knapsack_dp())