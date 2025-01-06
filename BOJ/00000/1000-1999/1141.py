class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.head = Node(None)
    
    def insert(self, string):
        cur_node = self.head
        
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
        
        cur_node.data = string
    
    def search(self, string):
        cur_node = self.head
        
        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
        
        return True

def solve():
    n = int(input())
    arr = list(set([input() for _ in range(n)]))
    arr.sort(key= lambda x: (-len(x), x))
    
    count = 0
    trie = Trie()
    for string in arr:
        if not trie.search(string):
            trie.insert(string)
            count += 1
            
    print(count)
    
    
solve()