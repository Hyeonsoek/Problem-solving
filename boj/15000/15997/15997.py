win, draw, lose = range(3)

def solve():
    name = input().split()
    rate : dict[str, dict[str, list]] = {}
    for x in name:
        rate[x] = {}
    
    for _ in range(6):
        a, b, *rates = input().split()
        rate[a][b] = [*map(float, rates)]
        rate[b][a] = rate[a][b][::-1]
    
    matches = {}
    index = 0
    for x in range(3):
        for y in range(x + 1, 4):
            matches[index] = name[x], name[y]
            index += 1
    
    result = { x : 0.0 for x in name }
    score = { x : 0 for x in name }
    def brute(prob, index):
        if index == 6:
            sortedScore = sorted(score.items(), key=lambda x: x[1])
            nname, nscore = zip(*sortedScore)
            
            if nscore[0] == nscore[1] == nscore[2] == nscore[3]:
                for x in nname:
                    result[x] += prob / 2
                return
            
            if nscore[0] == nscore[1] == nscore[2]:
                for name, p in zip(nname, [prob / 3, prob / 3, prob / 3, prob]):
                    result[name] += p
                return
            
            if nscore[1] == nscore[2] == nscore[3]:
                for x in nname[1:]:
                    result[x] += prob * 2 / 3
                return
            
            if nscore[1] == nscore[2]:
                for name, p in zip(nname, [0, prob / 2, prob / 2, prob]):
                    result[name] += p
                return
            
            for name, p in zip(nname, [0, 0, prob, prob]):
                result[name] += p
                
            return
        
        a, b = matches[index]
        if rate[a][b][win] != 0:
            score[a] += 3
            brute(prob * rate[a][b][win], index + 1)
            score[a] -= 3
        
        if rate[a][b][draw] != 0:
            score[a] += 1
            score[b] += 1
            brute(prob * rate[a][b][draw], index + 1)
            score[a] -= 1
            score[b] -= 1
            
        if rate[a][b][lose] != 0:
            score[b] += 3
            brute(prob * rate[a][b][lose], index + 1)
            score[b] -= 3
    
    brute(1, 0)
    
    for x in name:
        print(result[x])

solve()