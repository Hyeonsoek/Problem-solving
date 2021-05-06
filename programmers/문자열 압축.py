def solution(s):
    
    extract = []
    
    if len(s) == 1:
        return 1
    
    for dup_len in range(1, len(s)):
        
        start = 0
        extract_len = len(s)
        while start <= len(s) - dup_len*2:
            count = 1
            for idx in range(start + dup_len, len(s) - dup_len + 1, dup_len):
                if s[idx: idx+dup_len] == s[start : start+dup_len]:
                    count += 1
                else :
                    break
            if count > 1:
                start += count * dup_len
                extract_len -= ( dup_len * (count - 1) - len(str(count)) )
            else :
                start += dup_len
                
        extract.append(extract_len)
            
    return min(extract)