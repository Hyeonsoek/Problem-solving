# '1' ~ '899' =>
# (0~899) >
# (1~9 * 1)
# --------------
# (1~9 * 10) +
# (0~9 * 9)
# --------------
# (1~9 * 100) +
# (0~9 * 10 * 8 * 2)
# -------------
# (1~9 * 1000) +
# (0~9 * 100 * 9 * 3)

# 543
# 1~9 +1
# ------------
# 10~99
# 1~9 +10
# 0~9 +9
# ------------
# 100 ~ 499
# (1~4 * 100)
# (0~9 * 10 * 4)
# (0~9 * 10 * 4)
# -----------
# 500~539
# 0~3 * 10 | 0~9 * 4 and ['5'] * 40
# ----------
# 540~543
# 0~3 * 1 and ['5','4'] +4

# 14
# 1~9 +1
# =======
# 10 ~ 14
# 0~4 +1 // ['1'] +5

# 나중에 slice로도 풀어봐야겠다

def counter(val, result, cnt):
    while val > 0:
        result[val % 10] += cnt
        val //= 10

def solve():
    value = int(input())

    start = 1
    end = value
    digit = 1
    result = [0] * 10
    while start <= end:
        while start % 10 != 0 and start <= end:
            counter(start, result, digit)
            start += 1
        
        if start > end:
            break
            
        while end % 10 != 9 and start <= end:
            counter(end, result, digit)
            end -= 1
        
        count = end // 10 - start // 10 + 1
        for x in range(10):
            result[x] += count * digit
            
        start //= 10
        end //= 10
        digit *= 10
    
    print(*result)
    
solve()