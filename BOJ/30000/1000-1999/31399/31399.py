import sys
input = sys.stdin.readline
DRX = [-1, 0, 1, 0]
DRY = [0, 1, 0, -1]

def solve():
    H, W = map(int, input().split())
    R, C, D = map(int, input().split())

    def isinner(r, c):
        return 0 <= r < H and 0 <= c < W

    ruleA = [[*map(int, input().strip())] for _ in range(H)]
    ruleB = [[*map(int, input().strip())] for _ in range(H)]

    group = [[[0] * 4 for _ in range(W)] for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    
    index = 0
    result = 0
    while isinner(R, C):
        index += 1

        d = 0
        while isinner(R, C) and visited[R][C]:
            if group[R][C][D] == index:
                return result

            d += 1
            group[R][C][D] = index

            D = (D + ruleB[R][C]) % 4
            R += DRX[D]
            C += DRY[D]

        if isinner(R, C) and not visited[R][C]:
            result += d + 1
            visited[R][C] = True

            D = (D + ruleA[R][C]) % 4
            R = R + DRX[D]
            C = C + DRY[D]

    return result

print(solve())