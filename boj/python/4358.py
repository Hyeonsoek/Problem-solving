from sys import stdin
from collections import defaultdict

lines = stdin.readlines()
trees = defaultdict(int)

for line in lines:
    trees[line.strip()] += 1

name_ = list(sorted(trees.keys()))

for name in name_:
    print(name,  "{:.4f}".format(trees[name]/len(lines) * 100))