from collections import defaultdict


class Node(object):
    def __init__(self):
        self.data = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node.data += 1
            current_node = current_node.children[char]

    def search(self, string):
        current_node = self.head

        for char in string:
            if char == '?':
                break

            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return 0

        return current_node.data


def solution(words, queries):
    answer = []

    max_len = len(max(words, key=len))

    tries = [Trie() for _ in range(max_len)]
    rtries = [Trie() for _ in range(max_len)]

    for word in words:
        idx = len(word) - 1
        tries[idx].insert(word)
        rtries[idx].insert(word[::-1])

    for query in queries:
        result = None
        idx = len(query) - 1
        if idx >= max_len:
            answer.append(0)
            continue

        if query[0] == '?':
            result = rtries[idx].search(query[::-1])
        else:
            result = tries[idx].search(query)
        answer.append(result)

    return answer