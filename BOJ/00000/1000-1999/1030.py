def solve():
    s, n, k, R1, R2, C1, C2 = map(int, input().split())

    lengths = [n ** x for x in range(s + 1)]
    result = [[0] * (C2 - C1 + 1) for _ in range(R2 - R1 + 1)]

    def dnq(xx, yy, sx, sy, ex, ey, value, time):
        if time == 0:
            result[xx - R1][yy - C1] = value
        else:
            kdiv = (n - k) // 2
            # 다음 영역으로 분할
            length = lengths[time - 1]
            for xdiv in range(n):
                for ydiv in range(n):
                    nx = xx + xdiv * length
                    ny = yy + ydiv * length
                    
                    # 완전하게 벗어나는 경우
                    # 1) 색적 범위 끝값이 이번 영역의 시작점보다 작음
                    # 2) 색적 범위 시작값이 이 영역의 끝점보다 큼
                    if ex < nx or nx + length <= sx\
                            or ey < ny or ny + length <= sy:
                        continue
                
                    #영역 찢기
                    nsx = max(nx, sx)
                    nsy = max(ny, sy)
                    nex = min(nx + length - 1, ex)
                    ney = min(ny + length - 1, ey)
                    nvalue = 1 if value or (kdiv <= xdiv < kdiv + k and kdiv <= ydiv < kdiv + k) else 0
                    
                    dnq(nx, ny, nsx, nsy, nex, ney, nvalue, time - 1)
                
    dnq(0, 0, R1, C1, R2, C2, 0, s)

    for x in result:
        print(*x, sep='')
        
solve()