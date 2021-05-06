import re

def solution(s):
    answer = []
    tuples = re.findall(r'{[\d+,]*\d+}',s)
    
    for idx in range(len(tuples)):
        tuples[idx] = re.findall(r'\d+', tuples[idx])
    
    for x in range(len(tuples)):
        for y in range(len(tuples[x])):
            tuples[x][y] = int(tuples[x][y])
            
    tuples.sort(key=lambda x : len(x))
    if len(tuples) == 1:
        return tuples[0]
    
    for x in range(len(tuples)-1,0,-1):
        for y in range(len(tuples[x-1])):
            tuples[x].remove(tuples[x-1][y])
    
    for t in tuples:
        answer.append(t[0])
    
    return answer