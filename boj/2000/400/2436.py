gcd, lcm = map(int, input().split())

divisors = set()
ab = lcm * gcd
sqrt_ab = int(ab ** 0.5)
for x in range(1, sqrt_ab + 1):
    if lcm % x == 0:
        divisors.add(x)

def GCD(a, b) -> int:
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
def LCM(a, b) -> int:
    return int((a * b) / GCD(a, b))

result = []
for left in divisors:
    right = int(ab / left)
    ggcd = GCD(left, right)
    llcm = LCM(left, right)

    if ggcd == gcd and llcm == lcm:
        result.append((left, right))

ans_left, ans_right = 100000000, 100000000
for left, right in result:
    if left + right < ans_left + ans_right:
        ans_right = right
        ans_left = left

print(ans_left, ans_right)