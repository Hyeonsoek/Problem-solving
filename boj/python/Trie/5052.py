from sys import stdin

class Node(object):
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
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
            if cur_node.data is not None:
                return False

            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return True

        return True


T = int(input())

for _ in range(T):
    n = int(input())

    string_list = []
    for _ in range(n):
        string_list.append(stdin.readline().strip())
    string_list.sort(key=lambda x: len(x))

    check = True
    trie = Trie()
    for s in string_list:
        if trie.search(s):
            trie.insert(s)
        else:
            check = False
            break

    print("YES" if check else "NO")