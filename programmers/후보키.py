from collections import defaultdict
from itertools import combinations

def unique(combi):
    global index, column, row

    temp = [ "" for x in range(row) ]

    for x in combi:
        for y in range(row):
            temp[y] += str(index[x][y])

    if row == len(set(temp)):
        return True
    return False

def minimal(combi):
    global checks

    for check in checks:
        if len(combi) >= len(check):
            cnt = len(combi)
            for c in combi:
                if c in check:
                    cnt -= 1
            if cnt == len(combi) - len(check):
                return False

    return True


def solution(relation):
    answer = 0

    global index, checks, column, row

    index = defaultdict(list)
    column = len(relation[0])
    row = len(relation)
    index_list = [ x for x in range(column) ]

    for x in relation:
        for y in range(len(x)):
            index[y].append(x[y])

    checks = []

    for x in range(column):
        combi = list(combinations(index_list, x+1))

        for x in combi:
            if minimal(x) and unique(x):
                checks.append(x)
                answer += 1

    return answer

print(solution([["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","4"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]))

print(solution([['a',1,'aaa','c','ng'],
                ['b',1,'bbb','c','g'],
                ['c',1,'aaa','d','ng'],
                ['d',2,'bbb','d','ng']]))