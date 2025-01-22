i = 1
while (s := input()) != "0 0 0":
    p, l, v = map(int, s.split())
    print(f"Case {i}: {p * (v // l) + min(p, v % l)}")
    i += 1