from datetime import datetime as f
y,m,d=map(int,input().split())
e=f(*map(int,input().split()))
print(['gg',f'D{(f(y,m,d)-e).days}'][f(y+1000,m,d)>e])