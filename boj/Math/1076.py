colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
d = {x: 10 ** i for i, x in enumerate(colors)}
c = {x: str(i) for i, x in enumerate(colors)}
print(int(c[input()]+c[input()]) * d[input()])