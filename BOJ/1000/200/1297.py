d, h, w = map(int, input().split())
v = (h * h + w * w) ** .5
rate = d / v
print(int(h * rate), int(w * rate))