a, p, b, e, c = input().split()
d = eval(str(eval(a + p + b)) + e + c)
print("=================")
print("|SASA CALCULATOR|")
print(f"|{d:>15.3f}|")
print("-----------------")
print("|               |")
print("| AC         /  |")
print("| 7  8  9    *  |")
print("| 4  5  6    -  |")
print("| 1  2  3    +  |")
print("|    0  .    =  |")
print("=================")