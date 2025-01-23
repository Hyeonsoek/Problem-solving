string = input()

index = 0
UCPC = ['U', 'C', 'P', 'C']
for latter in string:
    if latter == UCPC[index]:
        index += 1
    
    if index == 4:
        break

print('I love UCPC' if index == 4 else 'I hate UCPC')