n, m = map(int, input().split())
hh, mm = divmod(m / n * 1440, 60)
print(f'{int(hh):02d}:{int(mm):02d}')