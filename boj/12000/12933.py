def sovle():
    string = input()
    duck = "quack"

    result = 0
    for _ in range(501):
        stack = []
        next = []
        for x in string:
            if x == duck[len(stack)]:
                stack.append(x)
            else:
                next.append(x)
            
            if "".join(stack[-5:]) == duck:
                for x in range(5):
                    stack.pop()
        
        if not stack:
            result += 1
        else:
            return -1
        
        string = "".join(next)
        
        if not string:
            return result
    
    return -1

print(sovle())