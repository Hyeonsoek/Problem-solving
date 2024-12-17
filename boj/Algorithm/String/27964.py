n = int(input())
arr = sum(map(lambda x: x[-6:] == "Cheese", set(input().split())))
print("yummy" if arr >= 4 else "sad")