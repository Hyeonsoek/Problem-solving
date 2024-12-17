from datetime import datetime as f
s=f(*map(int,input().split()))
e=f(*map(int,input().split()))
t = s - e
print(['gg', f'D{t.days}'][s > f(e.year - 1000, e.month, e.day)])