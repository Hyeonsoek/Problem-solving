import sys
input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]
    
    def getprefix(F, B):
        prefix = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if (i + j) & 1:
                    prefix[i][j] += board[i-1][j-1] != B
                else:
                    prefix[i][j] += board[i-1][j-1] != F
                prefix[i][j] += prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

        count = sys.maxsize
        for i in range(K, N + 1):
            for j in range(K, M + 1):
                count = min(count, prefix[i][j] - prefix[i][j-K] - prefix[i-K][j] + prefix[i-K][j-K])
        
        return count

    print(min(getprefix('W', 'B'), getprefix('B', 'W')))

solve()