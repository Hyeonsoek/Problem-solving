# https://sklubmk.github.io/2021/07/15/28bed7b50dc1/ 참고...

import heapq
from collections import defaultdict

def solution(n, start, end, roads, traps):
    
    traps_dict = {trap-1:idx for idx, trap in enumerate(traps)}
    board = [[] for _ in range(n)]
    check = [[False] * n for _ in range(1<<len(traps))]
    
    for s, e, cost in roads:
        board[s-1].append((e-1, cost, 0))
        board[e-1].append((s-1, cost, 1))

    heap = [(0, start-1, 0)]

    while heap:
        cost, vertex, state = heapq.heappop(heap)

        next_state = state
        isTrap = True if vertex in traps_dict else False

        if vertex == end-1:
            return cost

        if check[state][vertex]:
            continue
        else:
            check[state][vertex] = True

        for next_vertex, next_cost, road_type in board[vertex]:

            next_state = state
            next_isTrap = True if next_vertex in traps_dict else False

            if not (isTrap or next_isTrap):
                if road_type == 1:
                    continue
            elif isTrap and next_isTrap:
                nowisTrapOn = (state & (1 << traps_dict[vertex])) >> traps_dict[vertex]
                nextisTrapOn = (state & (1 << traps_dict[next_vertex])) >> traps_dict[next_vertex]

                if (nowisTrapOn ^ nextisTrapOn) != road_type:
                    continue
            else:
                index = vertex if isTrap else next_vertex
                isTrapOn = (state & (1 << traps_dict[index])) >> traps_dict[index]

                if isTrapOn != road_type:
                    continue

            if next_isTrap:
                next_state = state ^ (1 << traps_dict[next_vertex])

            heapq.heappush(heap, (cost + next_cost, next_vertex, next_state))

    return -1


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))