from collections import defaultdict, deque

#list 형태로 사용 시에 속도가 더 빠름
#기억을 되듬는 중....

def BFS(n : int, graph: defaultdict(list)) -> str:
    
    result = [x for x in range(n + 1)]
    check = [False for _ in range(n + 1)]
    queue = deque()
    
    check[1] = True
    queue.append(1)
    
    while(len(queue) > 0):
        value = queue.popleft()
        
        for x in graph[value]:
            if check[x] == False:
                check[x] = True
                result[x] = value
                queue.append(x)
    
    return '\n'.join(map(str, result[2:]))
    

if __name__ == "__main__":
    n = int(input())

    graph = defaultdict(list)

    for _ in range(n-1):
        front, end = map(int, input().split())
        
        graph[front].append(end)
        graph[end].append(front)
    
    print(BFS(n, graph))