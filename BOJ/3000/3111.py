word = input()
text = input()

len_word = len(word)
fp, ep = 0, len(text)-1
fs, es = [], []

while fp <= ep:
    while fp <= ep:
        fs.append(text[fp])
        fp += 1

        if len(fs) >= len(word) and ''.join(fs[-len_word:]) == word:
            for _ in range(len_word):
                fs.pop()
            break

    while fp <= ep:
        es.append(text[ep])
        ep -= 1

        if len(es) >= len(word) and ''.join(es[-len_word:]) == word[::-1]:
            for _ in range(len_word):
                es.pop()
            break

stack = ''.join(fs + es[::-1])

while word in stack:
    idx = stack.find(word)
    stack = stack[:idx] + stack[idx + len_word:]

print(stack)