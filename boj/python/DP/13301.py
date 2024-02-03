c=[0,4,6,*[0]*80]
for x in range(3,81):
    c[x]=c[x-1]+c[x-2]
print(c[int(input())])