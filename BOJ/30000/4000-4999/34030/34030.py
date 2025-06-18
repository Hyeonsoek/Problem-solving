import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [*map(int, input().split())]
    
    groupsP = []
    groupsV = [[], []]
    index = 0
    while index < n:
        group = []
        r = arr[index] % 2
        while index < n and arr[index] % 2 == r:
            group.append(arr[index])
            index += 1
        
        groupsV[r].extend(group)
        groupsP.extend(sorted(group))

    print("So Lucky" if groupsV[0] == sorted(groupsV[0]) and groupsV[1] == sorted(groupsV[1]) else "Unlucky")
    print("So Lucky" if groupsP == sorted(arr) else "Unlucky")

solve()