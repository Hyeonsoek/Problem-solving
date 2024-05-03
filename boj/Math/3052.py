array = [0] * 42
for _ in range(10):
    array[int(input())%42]+=1
print(sum(map(lambda x:1 if x>0 else 0, array)))