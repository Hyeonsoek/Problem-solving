import re
from itertools import permutations

def calcu(nums, s):
    fir = int(nums[0])
    sec = int(nums[1])
    if s == '*':
        return fir * sec
    if s == '-':
        return fir - sec
    if s == '+':
        return fir + sec
    
def solution(expression):
    answer = []
    
    priority = permutations(['+','-','*'],3)
    
    nums = re.findall(r'\d+', expression)
    operation = re.findall(r'[+*-]', expression)

    for p in priority:
        copy_nums = nums[:]
        copy_oper = operation[:]
        for s in p:
            idx = 0
            while len(copy_oper) > idx:
                if s == copy_oper[idx]:
                    result = calcu(copy_nums[idx:idx+2], s)
                    del copy_nums[idx:idx+2]
                    del copy_oper[idx]
                    copy_nums.insert(idx, str(result))
                else:
                    idx += 1
        answer.append(abs(int(copy_nums[0])))
    return max(answer)