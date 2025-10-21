import sys
MAX = 10 ** 9 + 1
input = sys.stdin.readline

def solve():
    """
    코드부터 읽는 사람들을 위한 설명
    v : 행렬합 저장하는 배열. 0 ~ n-1 : 행 / n ~ n+m : 열

    0이 아닌 행 혹은 열 중에 최솟값만 선택하는 Greedy로 작성
    최솟값 선택후에 행렬합들은 업데이트 해줘야 함
    """
    n, m = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(n)]

    v = [0] * (n + m)
    for x in range(n):
        for y in range(m):
            v[x] += board[x][y]

    for y in range(m):
        for x in range(n):
            v[y + n] += board[x][y]

    result = 1
    for i in range(n + m):
        c, x = MAX, 0
        for j in range(n + m):
            if v[j] > 0 and c > v[j]:
                c = v[j]
                x = j

        if c < MAX:
            v[x] = 0
            result = max(result, c)

        for j in range(n + m):
            if v[j] > 0:
                if x < n and j >= n:
                    v[j] -= board[x][j - n]
                
                if x >= n and j < n:
                    v[j] -= board[j][x - n]
        
    print(result)

solve()