def bracket_value(string):
	if len(string) == 2:
		if string == '()':
			return 2
		if string == '[]':
			return 3
	else:
		answer = 0
		stack = []
		strings = []
		temp = ''

		for x in list(string):
			if len(stack) == 0:
				strings.append(temp)
				temp = ''
				stack.append(x)
			else:
				top = stack[-1]
				if top == '(':
					if x == ')':
						stack.pop()
					if x == '(' or x == '[':
						stack.append(x)
				if top == '[':
					if x == ']':
						stack.pop()
					if x == '(' or x == '[':
						stack.append(x)
			temp += x
		strings.append(temp)

		for s in strings:
			if s:
				if len(s) == 2:
					answer += bracket_value(s)
					continue
				if s[0] == '(' and s[-1] == ')':
					answer += 2*bracket_value(s[1:-1])
				if s[0] == '[' and s[-1] == ']':
					answer += 3*bracket_value(s[1:-1])

		return answer

def bracket_true(string):
	stack = []

	for x in list(string):
		if len(stack) == 0:
			stack.append(x)
		else:
			top = stack[-1]
			if top == '(':
				if x == ')':
					stack.pop()
				if x == '(' or x == '[':
					stack.append(x)
			if top == '[':
				if x == ']':
					stack.pop()
				if x == '(' or x == '[':
					stack.append(x)
	if stack:
		return 0
	else:
		return 1

bracket = input()
if bracket_true(bracket):
	print(bracket_value(bracket))
else:
	print(0)
