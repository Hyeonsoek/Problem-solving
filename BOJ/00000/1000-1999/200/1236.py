#변태같은 숏코딩을 해보았다!

n,m=map(int,input().split())
b=[input()for _ in range(n)]
l=lambda x:0 if'X'in x else 1
c=sum(map(l,b))
r=sum(map(l,zip(*b)))
print(r if r>c else c)