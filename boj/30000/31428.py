n=int(input())
x={'I':0,'C':0,'S':0,'A':0}
for c in input().split():
    x[c]+=1
print(x[input()])