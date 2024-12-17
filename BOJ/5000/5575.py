from datetime import *

for x in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    s = timedelta(hours=sh, minutes=sm, seconds=ss)
    e = timedelta(hours=eh, minutes=em, seconds=es)
    r = (e - s).seconds
    print(r // 3600, (r // 60) % 60, r % 60)