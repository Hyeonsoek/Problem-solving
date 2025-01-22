def solve():
    n = int(input())
    dice = [*map(int, input().split())]

    if n == 1:
        return sum(dice) - max(dice)

    a, b, c, d, e, f = dice
    side = [b, c, e, d]

    three = 150
    for i in [a, f]:
        for j in [b, e]:
            for k in [c, d]:
                three = min(three, i + j + k)
    three *= 4
    
    two = 100
    for i in [a, f]:
        for j in side:
            two = min(two, i + j)
    
    for j in range(4):
        two = min(two, side[j] + side[(j + 1) % 4])
    two *= (8 * n - 12)
    
    one = min(dice) * (n - 2) * (5 * n - 6)
    
    return three + two + one

print(solve())