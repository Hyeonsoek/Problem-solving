w,h,p,q,t=map(int,open(0).read().split())
f=(p+t)%(2*w)
if f>w:f-=(f-w)*2
e=(q+t)%(2*h)
if e>h:e-=(e-h)*2
print(f,e)