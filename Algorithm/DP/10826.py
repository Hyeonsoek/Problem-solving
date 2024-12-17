c=[0]*10001
c[1]=1
for x in range(2, 10001):
    c[x]=c[x-1]+c[x-2]
print(c[int(input())])