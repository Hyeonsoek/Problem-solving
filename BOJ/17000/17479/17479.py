import sys
NORMAL = "NORMAL"
SPECIAL = "SPECIAL"
SERVICE = "SERVICE"
input = sys.stdin.readline

def solve():
    a, b, c = map(int, input().split())
    normal = {}
    for _ in range(a):
        name, cost = input().split()
        normal[name] = int(cost)
    
    special = {}
    for _ in range(b):
        name, cost = input().split()
        special[name] = int(cost)

    service = set([input().strip() for _ in range(c)])
    
    n = int(input())
    orders = [input().strip() for _ in range(n)]
    
    count = {NORMAL : 0, SPECIAL : 0, SERVICE : 0}
    cost = {NORMAL : 0, SPECIAL : 0}
    for order in orders:
        if order in normal:
            count[NORMAL] += 1
            cost[NORMAL] += normal[order]
        elif order in special:
            count[SPECIAL] += 1
            cost[SPECIAL] += special[order]
        elif order in service:
            count[SERVICE] += 1
    
    if cost[NORMAL] >= 20000:
        if cost[NORMAL] + cost[SPECIAL] >= 50000:
            if count[SERVICE] <= 1:
                return "Okay"
            return "No"
        else:
            if count[SERVICE] > 0:
                return "No"
            return "Okay"
    else:
        if count[SPECIAL] > 0 or count[SERVICE] > 0:
            return "No"
        return "Okay"

print(solve())