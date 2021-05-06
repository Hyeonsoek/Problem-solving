from bisect import bisect_left

def func(info_dict, value, cnt, start, now):
    if cnt == 0:
        if ''.join(now) in info_dict.keys():
            info_dict[''.join(now)].append(value)
        else:
            info_dict[''.join(now)] = [value]
    else :
        for s in range(start,4):
            temp = now[s]
            now[s] = '-'
            func(info_dict, value, cnt-1, s+1, now)
            now[s] = temp
            func(info_dict, value, cnt-1, s+1, now)

def solution(info, query):
    answer = []
    
    info_dict = {}
    
    for i in info:
        info_split = i.split()
        score = int(info_split[-1])
        attribute = info_split[:-1]
        
        func(info_dict, score, 4, 0, attribute)
    
    for key in info_dict:
        info_dict[key].sort()
    
    for q in query:
        q = q.replace(' and ','')
        key, value = q.split()
        
        if key in info_dict.keys():
            answer.append(len(info_dict[key]) - \
                bisect_left(info_dict[key], int(value), lo=0, hi=len(info_dict[key])))
        else:
            answer.append(0)
    
    return answer