def n_demical(n, k):
    if n > k:
        return chr(k%n+55) if k%n >= 10 else str(k%n)
    else:
        return n_demical(n, k//n) +\
                    (chr(k%n+55) if k%n >= 10 else str(k%n))

def solution(n, t, m, p):
    answer = ''

    demical = ""
    for x in range(t * m):
        demical += n_demical(n, x)

    idx = p-1
    while len(answer) < t:
        answer += demical[idx:idx+1]
        idx += m

    return answer