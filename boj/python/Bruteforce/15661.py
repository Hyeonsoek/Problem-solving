import sys, itertools
input = sys.stdin.readline
MAX = 10000000

n = int(input())
board = [ list(map(int, input().split())) for _ in range(n) ]

def team_value(team, length):
    tvalue = 0
    for x in range(length):
        for y in range(x + 1, length):
            tvalue += board[team[x]][team[y]]
            tvalue += board[team[y]][team[x]]
    
    opposite = list(set(range(0, n)) - set(team))
    for x in range(n - length):
        for y in range(x + 1, n - length):
            tvalue -= board[opposite[x]][opposite[y]]
            tvalue -= board[opposite[y]][opposite[x]] 
    
    return abs(tvalue)

def brute(team, idx, length):
    if length == n:
        return MAX
    
    result = team_value(team, length)
    for next in range(idx + 1, n):
        result = min(result, brute(team[:] + [next], next, length + 1))
    
    return result

print(brute([], -1, 0))