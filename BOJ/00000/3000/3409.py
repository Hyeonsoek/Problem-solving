import sys
input = sys.stdin.readline

def solve():
    k = int(input())
    tree : dict[str, list] = {}
    for _ in range(k):
        arr = input().strip().replace('+', '').replace('=', '').split()
        if len(arr) == 3:
            node, left, right = arr
            tree[node] = [left, right]
        else:
            node, value = arr
            tree[node] = [value]
    
    T = input().strip()
    P = input().strip()
    lenP = len(P)
    
    cache = {}
    for node in tree.keys():
        cache[node] = [-1] * (lenP + 1)
    
    def dynamic(node, index):
        if cache[node][index] != -1:
            return cache[node][index]
        
        if len(tree[node]) & 1:
            x = 0
            word = tree[node][0]
            while x < len(word) and index < lenP:
                if word[x] == P[index]:
                    index += 1
                x += 1
            return index
        
        left, right = tree[node]
        cache[node][index] = dynamic(right, dynamic(left, index))
        return cache[node][index]
    
    return "YES" if dynamic(T, 0) == len(P) else "NO"
    
t = int(input())
for _ in range(t):
    print(solve())