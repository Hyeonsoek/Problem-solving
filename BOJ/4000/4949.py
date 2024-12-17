import sys, itertools
input = sys.stdin.readline

def balance(string):
    large = []
    for i in string:
        if (i=='[') or (i=='('):
            large.append(i)
        elif i==']':
            if len(large)==0:
                large.append(i)
                break
            else:
                if large[-1]=='[':
                    large.pop()
        elif i==')':
            if len(large)==0:
                large.append(i)
                break
            else:
                if large[-1]=='(':
                    large.pop()

    if len(large)==0:
        return 'yes'
    else:
        return 'no'

# while True:
    # string = input().rstrip()
    
    # if string == '.':
    #     break
    
def balance2(string):
    stack = []
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(char)
                break
    
    # print("yes" if not stack else "no")
    return "yes" if not stack else "no"

strings = itertools.product(['(', ')', '[', ']'], repeat = 7)

for string in strings:
    string = ''.join(string)
    # print(string)
    if balance(string) != balance2(string):
        print(string)