def operate(a, b, op):
    match op:
        case "+":
            return a + b
        case "*":
            return a * b
        case "-":
            return a - b

def solve():
    n = int(input())
    expr = list(input())
    number = list(map(int, expr[::2]))
    operator = expr[1::2]

    count = len(operator)

    def brute(index, value):
        if index == count:
            return value
        else:
            b = number[index + 1]
            op = operator[index]
            
            result = brute(index+1, operate(value, b, op))
            
            if index + 2 <= count:
                c, op2 = number[index + 2], operator[index + 1]
                before = operate(b, c, op2)
                next = operate(value, before, op)
                result = max(result, brute(index + 2, next))
                
            return result

    print(brute(0, number[0]))
        
solve()

# 0 2 3 4 5
# 0 1 3 4 5