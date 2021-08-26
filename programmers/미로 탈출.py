# 미완성 코드, 보면서 공부 중

import heapq
from collections import defaultdict

def solution(n, start, end, roads, traps):
    
    traps_dict = {trap-1:idx for idx, trap in enumerate(traps)}
    board = [[] for _ in range(n)]
    check = [[0] * n for _ in range(1<<len(traps))]
    
    for s, e, cost in roads:
        board[s-1].append((e-1, cost, 0))
        board[e-1].append((s-1, cost, 1))

    heap = [(0, start, 0)]

    while heap:
        cost, vertex, state = heapq.heappop(heap)

        next_state = state
        isTrap = True if vertex in traps else False

        if vertex == end:
            return cost

        if check[state][vertex] == 1:
            continue
        else:
            check[start][vertex] = True

        for next_vertex, next_cost, road_type in board[vertex]:
            next_isTrap = True if (next_vertex+1) in traps else False

            if not next_isTrap:



# print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
# print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))