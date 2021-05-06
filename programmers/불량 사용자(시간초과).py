def permutation(value, idx, now, result, n):
    if idx == len(value):
        temp = sorted(list(set(now[:])))
        if (temp not in result) and len(temp) == n:
            result.append(temp)
    else:
        if value[idx][0] > 0:
            for x in range(len(value[idx][1])):
                value[idx][0] -= 1
                now.append(value[idx][1][x])
                permutation(value, idx, now, result, n)
                now.pop()
                value[idx][0] += 1
        elif value[idx][0] == 0:
            permutation(value, idx+1, now, result, n)

def solution(user_id, banned_id):
    answer = 0
    
    banned_star_idx = []
    banned_dict = {}
    for idx in range(len(banned_id)):
        temp = []
        loc = banned_id[idx].find('*',0)
        while loc != -1:
            temp.append(loc)
            loc = banned_id[idx].find('*', loc+1)
        banned_star_idx.append(temp)
        
        if banned_id[idx] in banned_dict:
            banned_dict[banned_id[idx]][0] += 1
        else :
            banned_dict[banned_id[idx]] = [1, []]
    
    for x in range(len(user_id)):
        for y in range(len(banned_id)):
            if len(user_id[x]) < len(banned_id[y]):
                continue
            yy = banned_id[y].replace('*','')
            xx = list(user_id[x])
            for z in range(len(banned_star_idx[y])):
                xx[banned_star_idx[y][z]] = ''
            xx = ''.join(xx)
            
            if xx == yy:
                banned_dict[banned_id[y]][1].append(user_id[x])
    
    now, result = [], []
    n = len(banned_id)
    permutation(list(banned_dict.values()), 0, now, result, n)
            
        
    return len(result)