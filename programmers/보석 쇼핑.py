def solution(gems):
    
    gems_dict = {gems[0]:1}
    answer = [1,100001]
    front, back = 1, 1
    n = len(gems)
    count = len(set(gems))
    
    while back-1 < n and front-1 < n:
        if len(gems_dict) == count:
            if answer[1] - answer[0] > back - front:
                answer = [front, back]
            gems_dict[gems[front-1]] -= 1
            if gems_dict[gems[front-1]] == 0:
                gems_dict.pop(gems[front-1])
            front += 1
        else :
            back += 1
            if back - 1 < n:
                if gems[back-1] in gems_dict:
                    gems_dict[gems[back-1]] += 1
                else :
                    gems_dict[gems[back-1]] = 1
    
    return answer