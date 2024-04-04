N, L, W, H = map(int, input().split())

low, high = 0, max(L, W, H)
for _ in range(100):
    if high < low:
        continue
    
    mid = (low + high) / 2
    count = int((L // mid) * (W // mid) * (H // mid))
    
    if count < N:
        high = mid
    else:
        low = mid

print(low)