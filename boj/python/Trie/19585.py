import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, end = False, data = ''):
        self.data = data
        self.end = end
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.head = Node()
    
    def insert(self, string):
        head = self.head
        
        for index, char in enumerate(string):
            if char not in head.children:
                head.children[char] = Node(False, char)
            
            head = head.children[char]
            
            if head.end == False:
                head.end = index == len(string) - 1
    
    def search(self, string):
        head = self.head
        
        for index, char in enumerate(string):
            if char in head.children:
                head = head.children[char]
                
                if head.end and string[index + 1:] in s:
                    return True
            else:
                break
        
        return False

trie = Trie()

n, m = map(int, input().split())
for _ in range(n):
    trie.insert(input().rstrip())

s = set([ input().rstrip() for _ in range(m) ])

q = int(input())
for _ in range(q):
    team_name = input().rstrip()
    print("Yes" if trie.search(team_name) else "No")