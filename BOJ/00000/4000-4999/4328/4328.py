while '0'!=(i:=input()):
    b,p,m=i.split()
    b=int(b)
    r=int(p,b)%int(m,b)
    t=''
    while r>=b:
        t+=str(r%b)
        r//=b
    print(str(r)+t[::-1])