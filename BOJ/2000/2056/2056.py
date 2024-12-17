import sys
input = sys.stdin.readline

class Node:
    def __init__(self, time, pre):
        self.time = time
        self.pre = pre

def solve():
    n = int(input())
    data : list[Node] = [Node(0, [])]
    for _ in range(n):
        t, c, *arr = map(int, input().split())
        data.append(Node(t, arr))
    
    cache = {1: data[1].time}
    def dynamic(node):
        if node in cache:
            return cache[node]
        
        result = 0
        for x in data[node].pre:
            result = max(result, dynamic(x))
        
        cache[node] = result + data[node].time
        return cache[node]
    
    result = 0
    for x in reversed(range(1, n + 1)):
        if x not in cache:
            result = max(result, dynamic(x))
    
    print(result)

solve()