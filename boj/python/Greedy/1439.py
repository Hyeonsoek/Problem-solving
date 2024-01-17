s = input()
z=[x for x in s.split('1') if x]
o=[x for x in s.split('0') if x]
lz,lo=len(z),len(o)
print(lz if lz < lo else lo)