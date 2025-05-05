import sys
vowels = ['a', 'e', 'i', 'o', 'u']

def hasVowel(word):
    for i in word:
        if i in vowels:
            return True
    return False

def isContinuous(word, isConsonant):
    isVowels = [0] * len(word)
    for i in range(len(word)):
        isVowels[i] = int((word[i] in vowels) ^ isConsonant)
    for i in range(1, len(word)):
        if isVowels[i] > 0:
            isVowels[i] += isVowels[i - 1]
        if isVowels[i] >= 3:
            return False
    return True

def isValid(word):
    if not hasVowel(word):
        return False
    if not isContinuous(word, True) or not isContinuous(word, False):
        return False
    for i in range(1, len(word)):
        if word[i] == word[i - 1] and word[i] not in ['e', 'o']:
            return False
    return True

for line in sys.stdin:
    word = line.strip()
    if word == 'end':
        break
    if isValid(word):
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')