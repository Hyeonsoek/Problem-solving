def solution(words):
    answer = 0
    
    trie = {}
    for word in words:
        now_trie = trie
        for letter in word:
            now_trie.setdefault(letter, [0, {}])
            now_trie[letter][0] +=1              
            now_trie = now_trie[letter][1]
            
    for word in words:

        j = 0
        now_trie = trie

        while j < len(word):
            if word[j] not in now_trie or now_trie[word[j]][0] == 1:
                break
            now_trie = now_trie[word[j]][1]
            j += 1

        if j == len(word):
            answer += j
        else:
            answer += (j+1)
    
    return answer