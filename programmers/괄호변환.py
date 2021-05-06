def corrected(x):
    stack = []
    for idx in range(len(x)):
        if x[idx] == '(':
            stack.append(x[idx])
        elif x[idx] == ')' and len(stack) > 0 :
            stack.pop(-1)
    
    return True if not stack else False

def balanced(x):
    left, right = 0, 0
    for char in x:
        if char == '(':
            left += 1
        else :
            right += 1
    return left == right

def revers(x):
    l = []
    for y in x:
        l += '(' if y == ')' else ')'
    return ''.join(l)

def func(w):
    if w == "":
        return ""
    
    if corrected(w):
        return w
    
    for idx in range(1,len(w)+1):
        if balanced(w[:idx]) and balanced(w[idx:]):
            if corrected(w[:idx]):
                return w[:idx] + func(w[idx:])
            else :
                return "(" + func(w[idx:]) + ")" + revers(w[:idx][1:-1])
            
def solution(p):
    print(revers(p))
    answer = func(p)
    return answer